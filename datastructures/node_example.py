from Nodes import Node

malcom_value = {
    "txId": "09asd0a9sd09ad9a0dahdadnjadjand",
    "amount": 900,
    "sender": "malcom",
    "receiver": "john"
}

john_value = {
    "txId": "09asd0a9sd09ad9a0dahdadnjadjand",
    "amount": 900,
    "sender": "",
    "receiver": "john"
}

malcom_node = Node(value=malcom_value)
john_node = Node(value=john_value)

malcom_node.set_next_node(john_node)
john_node.set_previous_node(malcom_node)


john_node.show()


