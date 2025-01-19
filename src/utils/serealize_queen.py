import uuid


def serialize_queen(queen):
    data = queen.__dict__.copy()

    data.pop('_sa_instance_state', None)

    if isinstance(data.get('id'), uuid.UUID):
        data['id'] = str(data['id'])

    if isinstance(data.get('solutions'), list):
        data['solutions'] = [str(solution) for solution in data['solutions']]

    return data
