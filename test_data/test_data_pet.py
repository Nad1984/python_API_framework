test1 = ("sold", "available", "pending")
keys = ("id", "name", "category", "photoUrls", "tags", "status")
test2 = (("sold", ("id", "name", "category", "photoUrls", "tags", "status")),
         ("available", ("id", "name", "category", "photoUrls", "tags", "status")),
         ("pending", ("")))
test3 = (({
    "id": 10,
    "name": "doggie",
    "category": {
        "id": 1,
        "name": "Dogs"
    },
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 1,
            "name": "super puper"
        }
    ],
    "status": "sold"
}),
         ({
             "id": 11,
             "name": "PusyMusi",
             "category": {
                 "id": 2,
                 "name": "Dogs"
             },
             "photoUrls": [
                 "https://www.pexels.com/photo/short-coated-tan-dog-2253275/"
             ],
             "tags": [
                 {
                     "id": 2,
                     "name": "shock"
                 }
             ],
             "status": "available"
         }),
         ({
             "id": 12,
             "name": "Fluffy",
             "category": {
                 "id": 3,
                 "name": "Dogs"
             },
             "photoUrls": [
                 "string"
             ],
             "tags": [
                 {
                     "id": 3,
                     "name": "quite"
                 }
             ],
             "status": "available"
         }))
test4 = (({
    "id": 10,
    "name": "Pusik",
    "category": {
        "id": 1,
        "name": "Dogs"
    },
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 1,
            "name": "super puppy"
        }
    ],
    "status": "sold"
}),
         ({
             "id": 11,
             "name": "Sharik",
             "category": {
                 "id": 2,
                 "name": "Dogs"
             },
             "photoUrls": [
                 "https://www.pexels.com/photo/short-coated-tan-dog-2253275/"
             ],
             "tags": [
                 {
                     "id": 2,
                     "name": "shock"
                 }
             ],
             "status": "available"
         }),
         ({
             "id": 12,
             "name": "Fluffy grace",
             "category": {
                 "id": 3,
                 "name": "Dogs"
             },
             "photoUrls": [
                 "string"
             ],
             "tags": [
                 {
                     "id": 3,
                     "name": "quite"
                 }
             ],
             "status": "pending"
         }))
test5 = ((10, "Pusik"), (11, "Sharik"), (12, "Fluffy grace"))
test6 = ("super puppy", "quite", "shock")
test7 = ("", "AvailabLe", "~!#@$$%&^*789423")
test8 = ((({
    "id": "$elect*",
    "name": "Pusik",
    "category": {
        "id": 1,
        "name": "Dogs"
    },
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 1,
            "name": "super puppy"
        }
    ],
    "status": "sold"
}), 400),
         (({
             "id": 1234567890,
             "name": "Sharik",
             "category": {
                 "id": 2,
                 "name": "Dogs"
             },
             "photoUrls": [
                 "https://www.pexels.com/photo/short-coated-tan-dog-2253275/"
             ],
             "tags": [
                 {
                     "id": 2,
                     "name": "shock"
                 }
             ],
             "status": "available"
         }), 404),
         (({
             "id": "***",
             "name": "Fluffy grace",
             "category": {
                 "id": 3,
                 "name": "Dogs"
             },
             "photoUrls": [
                 "string"
             ],
             "tags": [
                 {
                     "id": 3,
                     "name": "quite"
                 }
             ],
             "status": "pending"
         }), 400))
