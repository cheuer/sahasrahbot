from ..util import orm

async def insert_spoiler_race(srl_id, spoiler_url):
    await orm.execute(
        'INSERT INTO spoiler_races(srl_id, goal) VALUES (%s,%s) ON DUPLICATE KEY UPDATE spoiler_url = %s;',
        [srl_id, spoiler_url, spoiler_url]
    )

async def delete_spoiler_race(srl_id):
    await orm.execute(
        'DELETE FROM spoiler_races WHERE srl_id=%s;',
        [srl_id]
    )

async def get_spoiler_races():
    results = await orm.select(
        'SELECT * from spoiler_races;'
    )
    return results

async def get_spoiler_race_by_id(srl_id):
    results = await orm.select(
        'SELECT * from spoiler_races where srl_id=%s;',
        [srl_id]
    )
    return results[0]