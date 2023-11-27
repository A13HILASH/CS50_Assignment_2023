

def convert(prompt):
    happy=":)"
    sad=":("
    prompt=prompt.replace(":)","🙂")
    prompt=prompt.replace(":(","🙁")
    
    return (prompt)
    









































def main():
    userinput=input()
    print(convert(userinput))
    



main()