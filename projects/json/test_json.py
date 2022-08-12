
def test__Contains_seventh_son_of_seventh_son():
    contains_seventh_son_of_seventh_son = {
        'name': 'A',
        'gender': 'male',
        'children': [
            {'name': 'B',
             'gender': 'male',
             'children': []},
            {'name': 'C',
             'gender': 'male',
             'children': []},
            {'name': 'D',
             'gender': 'male',
             'children': []},
            {'name': 'E',
             'gender': 'male',
             'children': []},
            {'name': 'F',
             'gender': 'male',
             'children': []},
            {'name': 'G',
             'gender': 'male',
             'children': []},
            {'name': 'H', # This is the seventh son
             'gender': 'male',
             'children':[
                {'name': 'I',
                 'gender': 'male',
                 'children': []},
                {'name': 'J',
                 'gender': 'male',
                 'children': []},
                {'name': 'K',
                 'gender': 'male',
                 'children': []},
                {'name': 'L',
                 'gender': 'male',
                 'children': []},
                {'name': 'M',
                 'gender': 'male',
                 'children': []},
                {'name': 'N',
                 'gender': 'male',
                 'children': []},
                {'name': 'O', # This is the sventh son of the seventh son
                 'gender': 'male',
                 'children': []}
             ]}
        ]
    }
    test.assert_equals(find_seventh_sons_of_seventh_sons(json.dumps(contains_seventh_son_of_seventh_son)), {'O'}) 

def test__Would_be_seventh_son_of_seventh_son_is_a_daughter():
    does_not_contain_seventh_son_of_seventh_son = {
        'name': 'A',
        'gender': 'male',
        'children': [
            {'name': 'B',
             'gender': 'male',
             'children': []},
            {'name': 'C',
             'gender': 'male',
             'children': []},
            {'name': 'D',
             'gender': 'male',
             'children': []},
            {'name': 'E',
             'gender': 'male',
             'children': []},
            {'name': 'F',
             'gender': 'male',
             'children': []},
            {'name': 'G',
             'gender': 'male',
             'children': []},
            {'name': 'H', # This is the seventh son
             'gender': 'male',
             'children':[
                {'name': 'I',
                 'gender': 'male',
                 'children': []},
                {'name': 'J',
                 'gender': 'male',
                 'children': []},
                {'name': 'K',
                 'gender': 'male',
                 'children': []},
                {'name': 'L',
                 'gender': 'male',
                 'children': []},
                {'name': 'M',
                 'gender': 'male',
                 'children': []},
                {'name': 'N',
                 'gender': 'male',
                 'children': []},
                {'name': 'O',
                 'gender': 'female', # The seventh son of the seventh son is in fact a daughter!
                 'children': []}
             ]}
        ]
    }
    test.assert_equals(find_seventh_sons_of_seventh_sons(json.dumps(does_not_contain_seventh_son_of_seventh_son)), set()) 

def test__Chain_of_sons_is_broken():
    does_not_contain_seventh_son_of_seventh_son = {
        'name': 'A',
        'gender': 'male',
        'children': [
            {'name': 'B',
             'gender': 'male',
             'children': []},
            {'name': 'C',
             'gender': 'male',
             'children': []},
            {'name': 'D',
             'gender': 'male',
             'children': []},
            {'name': 'E',
             'gender': 'female', # The chain of sons is broken!
             'children': []},
            {'name': 'F',
             'gender': 'male',
             'children': []},
            {'name': 'G',
             'gender': 'male',
             'children': []},
            {'name': 'H',
             'gender': 'male',
             'children':[
                {'name': 'I',
                 'gender': 'male',
                 'children': []},
                {'name': 'J',
                 'gender': 'male',
                 'children': []},
                {'name': 'K',
                 'gender': 'male',
                 'children': []},
                {'name': 'L',
                 'gender': 'male',
                 'children': []},
                {'name': 'M',
                 'gender': 'male',
                 'children': []},
                {'name': 'N',
                 'gender': 'male',
                 'children': []},
                {'name': 'O',
                 'gender': 'male',
                 'children': []}
             ]}
        ]
    }
    test.assert_equals(find_seventh_sons_of_seventh_sons(json.dumps(does_not_contain_seventh_son_of_seventh_son)), set()) 


def test__Seventh_son_does_not_have_children():
    does_not_contain_seventh_son_of_seventh_son = {
        'name': 'A',
        'gender': 'male',
        'children': [
            {'name': 'B',
             'gender': 'male',
             'children': []},
            {'name': 'C',
             'gender': 'male',
             'children': []},
            {'name': 'D',
             'gender': 'male',
             'children': []},
            {'name': 'E',
             'gender': 'female',
             'children': []},
            {'name': 'F',
             'gender': 'male',
             'children': []},
            {'name': 'G',
             'gender': 'male',
             'children': []},
            {'name': 'H', # This is the seventh son, but he has no children
             'gender': 'male',
             'children':[]
            }
        ]
    }
    test.assert_equals(find_seventh_sons_of_seventh_sons(json.dumps(does_not_contain_seventh_son_of_seventh_son)), set()) 
