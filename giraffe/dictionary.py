monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

key = input("Enter month key: ")
print("Full month name: " + monthConversions.get(key, "Not a valid key"))
print("Full month name: " + monthConversions[key])
