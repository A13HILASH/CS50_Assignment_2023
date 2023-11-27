#import emoji module.
import emoji
#Get user input.
userip=input("Input: ")
#Print emoiji returned by emojize function.
print(emoji.emojize(f'Output: {userip}',language='alias'))