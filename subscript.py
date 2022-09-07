import string

# function to convert to subscript

def subscript(letter):
    numbers=""
    for i in range(10): numbers +=str(i)
    normalString = string.ascii_lowercase + numbers
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    subString = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    sub = letter.maketrans(normal, subString)
    return letter.translate(sub)

# example_string = "A0B1C2D3E4F5G6H7I8J9"

# SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
# SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

# print(example_string.translate(SUP))
# print(example_string.translate(SUB))
if __name__ == "__main__":
    print("WW{}".format(subscript('9')))
