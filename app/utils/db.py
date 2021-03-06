import pymongo
import loader # noqa


def connect(client, db_name, db_collection_name):
    try:
        print('Connect: MongoDB version is %s' % client.server_info()['version'])
        db = client[db_name]
        db_collection = db[db_collection_name]
        return {
            'db': db,
            'collection': db_collection
        }
    except pymongo.errors.OperationFailure as error:  # noqa
        print(error)
        quit(1)


# ============ create
def add_user(message, db_collection):
    if db_collection.find_one({'user_telegram_id': message.from_user.id}) is None:
        user = {
            'user_telegram_id': message.from_user.id,
            'first_name': message.from_user.first_name,
            'last_name': message.from_user.last_name,
            'important': [],
            'ordinary': [],
            'notifications': True,
            'notification_interval': loader.DEFAULT_VALUE,
            'working_process': True
        }
        db_collection.insert_one(user)
        return True


# ============ get
def user_get_tasks(message, db_collection):
    result = {}
    tasks = db_collection.find_one({'user_telegram_id': message.from_user.id},
                                   {'important', 'ordinary'})
    if tasks.get('_id'):
        del tasks['_id']
    for key, value in tasks.items():
        if value:
            result[key] = value
        else:
            result[key] = None
    return result


def user_get_notifications(message, db_collection):
    result = db_collection.find_one({'user_telegram_id': message.from_user.id},
                                    {'notifications', 'notification_interval'})
    del result['_id']
    return result


# ============ set
def user_set_task(message, db_collection, current_list, current_task):
    result = db_collection.update_one({'user_telegram_id': message.from_user.id},
                                      {'$push': {current_list: current_task}})
    return result.acknowledged


# =========== del
def user_del_task(message, db_collection, task_list, task_id):
    result = db_collection.update_one({'user_telegram_id': message.from_user.id},
                                      {'$pull': {task_list: {'task_id': task_id}}})
    return result.acknowledged


# =========== update
def user_update_task(message, db_collection, task_list, task_index, user_task):
    result = db_collection.update_one(
        {'user_telegram_id': message.from_user.id},
        {'$set': {f'{task_list}.{task_index}': {'task_id': user_task['task_id'],
                                                'task_status': user_task['task_status'],
                                                'task': user_task['task']}}})
    return result.acknowledged


def user_update_notification(message, db_collection, field, status):
    result = db_collection.update_one(
        {'user_telegram_id': message.from_user.id},
        {'$set': {field: status}})
    return result.acknowledged

