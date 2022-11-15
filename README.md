# dialed_in_api

---

The CRUD api which handles data for my dialed in webapp. Currently being rewritten
in rust, because rocket is exciting and rust is fast(or so I've heard). Should support
JWT based authentication, and interface with a (mongoDB?) database. 

### Routes:

1. coffees
    - GET
    - POST
2. extractions
    - GET
    - POST
3. token
    - GET
    - /refresh
        - POST
4. register
    - GET
5. profile
    - GET
    - POST
6. api-auth
    -??? Figure out what this does again
