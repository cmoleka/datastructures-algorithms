from LinkedList import LinkedList

genesis_node = {
    "txId": "09asd0a9sd09ad9a0dahdadnjadjand",
    "amount": 900,
    "sender": "malcom",
    "receiver": "john"
}


node_0 = {
    "txId": "09asd0a9sd09ad9a0dahdadnjadjand",
    "amount": 900,
    "sender": "",
    "receiver": "john"
}

node_1 = {
    "txId": "ksdjaksjdkasjd88383",
    "amount": 2000,
    "sender": "john",
    "receiver": "laurence"
}
LinkedListInstance = LinkedList(genesis_node)
LinkedListInstance.insert_beginning(node_0)
LinkedListInstance.insert_beginning(node_1)
LinkedListInstance.remove_node(node_0)

print(LinkedListInstance.stringify_list())
