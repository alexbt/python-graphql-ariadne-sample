# source
- https://blog.sethcorker.com/how-to-create-a-react-flask-graphql-project

# Launch
- python src/sample/app.py
- http://127.0.0.1:5000 


# query
```
query {
    orders {
        id
        name
        type
        size
    }
}
```

# mutations
```
mutation {
    orderCoffee(size: REGULAR, name: "name", type: ESPRESSO) {
        id
        name
        type
        size
    }
}
```