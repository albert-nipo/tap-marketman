import singer
from datetime import timezone, datetime
from singer import Transformer, metadata
from tap_marketman.client import MarketManClient
from tap_marketman.streams import STREAMS

LOGGER = singer.get_logger()


def sync(config, state, catalog):
    client = MarketManClient()

    guids = client.get_guid()

    for guid in guids:
        with Transformer() as transformer:
            for stream in catalog.get_selected_streams(state):
                tap_stream_id = stream.tap_stream_id
                stream_obj = STREAMS[tap_stream_id](client, state)
                # replication_key = stream_obj.replication_key
                key = stream_obj.key_properties[0]
                stream_schema = stream.schema.to_dict()
                stream_metadata = metadata.to_map(stream.metadata)

                LOGGER.info('Staring sync for stream: %s', tap_stream_id)

                state = singer.set_currently_syncing(state, tap_stream_id)
                singer.write_state(state)

                singer.write_schema(
                    tap_stream_id,
                    stream_schema,
                    stream_obj.key_properties,
                    stream.replication_key
                )

                for record in stream_obj.records_sync(guid=guid):
                    transformed_record = transformer.transform(
                        record, stream_schema, stream_metadata)
                    LOGGER.info(f"Writing record: {transformed_record}")
                    singer.write_record(
                        tap_stream_id,
                        transformed_record,
                    )

                current_time = datetime.now(timezone.utc)

                singer.write_bookmark(
                    stream_obj.state,
                    tap_stream_id,
                    key,
                    current_time
                )

                LOGGER.info(
                    f'Bookmark created for {tap_stream_id} stream = {key}: {current_time}')


    state = singer.set_currently_syncing(state, None)
    singer.write_state(state)
