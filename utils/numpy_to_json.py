from typing import Any
import json
import orjson

class FastJSONEncoder(json.JSONEncoder):

    def encode(self, o: Any) -> str:
        return orjson.dumps(o, option=orjson.OPT_SERIALIZE_NUMPY,).decode('UTF-8')
