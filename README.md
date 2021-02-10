# MarketMan Tap

This is a [Singer](https://singer.io) tap that reads data from the [MarketMan API](https://api-doc.marketman.com/?version=latest#intro) and produces JSON-formatted data following the [Singer spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

## How to use it

`tap-marketman` works together with any other [Singer Target](https://singer.io) to move data from the MarketMan API to any target destination.

### Install

First, make sure Python 3 is installed on your system or follow these
installation instructions for [Mac](http://docs.python-guide.org/en/latest/starting/install3/osx/) or
[Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04).

This project is set up using [Python Poetry](https://python-poetry.org/). Once cloned and within the project directory, install dependencies with:

```bash
poetry install
```

## Configuration

Requirements to get started are API Credentials in the form of an APIKey and APIPassword.

The first portion of the tap is to pull all the GUIDs that are associated with the credentials.  This will allow the tap to iterate over these ids and pull data associate with the configured endpoints.

# Streams

## Full Table Streams
These Streams pull all the data each time they are run based on the endpoint.  Different targets can handle duplicate data differently.

[Inventory Items](https://api-doc.marketman.com/?version=latest#8dcfdaad-f9cc-4485-9504-62064a32a9ff)
- Primary key fields: ID
- Replication strategy: FULL_TABLE
- Transformations: none

[Menu Items](https://api-doc.marketman.com/?version=latest#51b60a8b-dce2-4784-9d20-7eb6b303025c)
- Primary key fields: ID
- Replication strategy: FULL_TABLE
- Transformations: none

[Preps](https://api-doc.marketman.com/?version=latest#de20f2e4-2a70-4901-ae5e-1e642165e869)
- Primary key fields: ID
- Replication strategy: FULL_TABLE
- Transformations: none


## Incremental Streams
These Streams pull data from between two timestamps.  Inital timestamps should be based on earliest needed times.  Each run resets this timestamp to the current run data and time.  Different targets can handle duplicate data differently.

[Inventory Counts](https://api-doc.marketman.com/?version=latest#561b8144-1ffe-43d5-b7c3-e3c9bfe66962)
- Primary key fields: ID
- Replication strategy: INCREMENTAL
- Replication based on: Start Date through End Date (Bookmarked)
- Transformations: none

[Waste Events](https://api-doc.marketman.com/?version=latest#b2b90898-cd9d-468d-8943-041de0bc48b2)
- Primary key fields: ID
- Replication strategy: INCREMENTAL
- Replication based on: Start Date through End Date (Bookmarked)
- Transformations: none

[Waste Events](https://api-doc.marketman.com/?version=latest#6de85108-2163-41e8-8215-8ecf38fd6671)
- Primary key fields: OrderNumber
- Replication strategy: INCREMENTAL
- Replication based on: Start Date through End Date (Bookmarked)
- Transformations: none