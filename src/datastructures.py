
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
            "id":4,
            "first_name":"Jose",
            "last_name": "MUro"},
            {"id":2,
            "first_name":"Joaqui",
            "last_name":"Vazquez"
            }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member["id"] = self._generateId()
        # fill this method and update the return        
        self._members.append(member)

    def delete_member(self, id):
        # fill this method and update the return
        for element in family.get_all_members():
            for e in element.values():
                if e == (id):
                    family.get_all_members().remove(element)

    def get_member(self, id):
        # fill this method and update the return
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

member = {
    "id":[],
    "first_name": "Peter",
    "last_name": "Jackson",
    "age": 44,
    "lucky_numbers": [{1,2,3}]
}


family= FamilyStructure(last_name="Jackson")
#print(family.last_name)
print(family.get_all_members())
family.delete_member(4)
print(family.get_all_members())


