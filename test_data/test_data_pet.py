test1 = ("sold", "available", "pending")
keys = ("id", "name", "category", "photoUrls", "tags", "status")
test2 = (("sold", ("id", "name", "category", "photoUrls", "tags", "status")),
         ("available", ("id", "name", "category", "photoUrls", "tags", "status")),
         ("pending", ("")))
test3 = (({
    "id": 11,
    "name": "PusyMusi",
    "category": {
        "id": 1,
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
                 "id": 1,
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
         }), ({
    "id": 13,
    "name": "Bad cat",
    "category": {
        "id": 2,
        "name": "Cats"
    },
    "photoUrls": [
        "URL5"
    ],
    "tags": [
        {
            "id": 22,
            "name": "sharp claw"
        }
    ],
    "status": "sold"
}))
test4 = (({
    "id": 13,
    "name": "Baddest cat",
    "category": {
        "id": 2,
        "name": "Cats"
    },
    "photoUrls": [
        "URL5"
    ],
    "tags": [
        {
            "id": 22,
            "name": "Sharpest claws"
        }
    ],
    "status": "sold"
}),
         ({
             "id": 11,
             "name": "Sharik",
             "category": {
                 "id": 1,
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
                 "id": 1,
                 "name": "Dogs"
             },
             "photoUrls": [
                 "url1",
                 "url2"
             ],
             "tags": [
                 {
                     "id": 3,
                     "name": "quite"
                 }
             ],
             "status": "pending"
         }))
test5 = ((13, "Baddest cat", 2, "Cats", 22, "Sharpest claws", ["URL5"], "sold"), (
    11, "Sharik", 1, "Dogs", 2, "shock", ["https://www.pexels.com/photo/short-coated-tan-dog-2253275/"], "available"),
         (12, "Fluffy grace", 1, "Dogs", 3, "quite", ["url1", "url2"], "pending"))
test6 = ("quite", "shock", "Sharpest claws")
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

test9 = (({
    "id": "",
    "name": "",
    "category": {
        "id": "",
        "name": ""
    },
    "photoUrls": [
        ""
    ],
    "tags": [
        {
            "id": "",
            "name": ""
        }
    ],
    "status": ""
}), ({
    "id": "",
    "name": "",
    "category": {
        "id": "",
        "name": ""
    },
    "photoUrls": [
        ""
    ],
    "tags": [
        {
            "id": "",
            "name": ""
        }
    ],
    "status": ""
}))

test10 = (({
    "id": "@#$#^%$&",
    "name": "",
    "category": {
        "id": "5",
        "name": ""
    },
    "photoUrls": [
        ""
    ],
    "tags": [
        {
            "id": "",
            "name": ""
        }
    ],
    "status": ""
}), ({
    "id": "sdfsfdd",
    "name": "",
    "category": {
        "id": "",
        "name": ""
    },
    "photoUrls": [
        ""
    ],
    "tags": [
        {
            "id": "",
            "name": ""
        }
    ],
    "status": ""
}), ({
    "id": False,
    "name": "",
    "category": {
        "id": "",
        "name": ""
    },
    "photoUrls": [
        ""
    ],
    "tags": [
        {
            "id": "",
            "name": ""
        }
    ],
    "status": ""
}))

test11 = (({
    "id": 13,
    "name": "Bad cat",
    "category": {
        "id": 2,
        "name": "Cats"
    },
    "photoUrls": [
        "URL5"
    ],
    "tags": [
        {
            "id": 22,
            "name": "sharp claw"
        }
    ],
    "status": "sold"
}), ({
    "id": 13,
    "name": "Bad cat",
    "category": {
        "id": 2,
        "name": "Cats"
    },
    "photoUrls": [
        "URL5"
    ],
    "tags": [
        {
            "id": 22,
            "name": "sharp claw"
        }
    ],
    "status": "sold"
}))
