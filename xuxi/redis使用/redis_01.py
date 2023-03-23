import redis
if __name__ == '__main__':
    try:
        rs = redis.Redis()
    except Exception as e:
        print(e)
    result = rs.set('name','itcast')
    print(result)
    name = rs.get('name')
    print(name)