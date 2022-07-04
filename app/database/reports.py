from uuid import RESERVED_FUTURE
from app.database import get_db


def output_formatter(results):
    out = []
    for results in results:
        user = {}
        user["last_name"] = result[0]
        user["first_name"] = result[1]
        user["hobbies"] = result[2]
        user["active"] = result[3]
        user["brand"] = result[4]
        user["model"] = result[5]
        user["license_plate"] = result[6]
        user["color"] = result[7]
        user["description"] = result[8]
        out.append(user)
    return out


def scan():
    cursor = get_db().execute(
        """SELECT user.last_name,
            user.first_name,
            user.hobbies,
            user.active,
            vehicle.license_plate,
            vehicle.color,
            vehicle_type.description,
            vehicle.brand,
            vehicle.model,
            FROM USER WHERE ACTIVE=1
            """, ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)
