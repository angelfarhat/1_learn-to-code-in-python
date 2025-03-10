#Complete each of the get_XXX_bits functions. Simply use the bitwise & operation on the input of the user's permission bits and the appropriate guild permission bits variable, and return the resulting bits for them to be checked by the tests.
#4 values have been provided, use the appropriate one for each function:

# can_create_guild
# can_review_guild
# can_delete_guild
# can_edit_guild
#Note: The get_XXX_bits functions return the bits and the test code compares the result to the original permission value to see if it matches!
can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001


def get_create_bits(user_permissions):
    op = user_permissions & can_create_guild
    return op


def get_review_bits(user_permissions):
    op = user_permissions & can_review_guild
    return op


def get_delete_bits(user_permissions):
    op = user_permissions & can_delete_guild
    return op    


def get_edit_bits(user_permissions):
    op = user_permissions & can_edit_guild
    return op   
