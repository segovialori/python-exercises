{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1.  Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#1.\n",
    "def is_two(x):\n",
    "    if x == 2 or x == '2':\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "is_two(3)\n",
    "is_two(2)\n",
    "is_two('2')\n",
    "\n",
    "#Zach way\n",
    "#is_two(anything)->bool\n",
    "def is_two(x):\n",
    "    return x == 2 or x == \"2\"\n",
    "is_two(1)\n",
    "is_two('2')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2.  Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#2.\n",
    "def is_vowel(x):\n",
    "    if x in 'aeiou':\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "\n",
    "is_vowel('a')\n",
    "\n",
    "is_vowel('l')\n",
    "\n",
    "#zach way\n",
    "#is_vowel (character:str)->bool\n",
    "def is_vowel(c):\n",
    "    return c.lower() in 'aeiou'\n",
    "\n",
    "is_vowel('b')\n",
    "\n",
    "#Diff between list and a string\n",
    "#python can loop through individual characters in a string\n",
    "#python will treat a string and list of characters mostly the same\n",
    "#"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3.  Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#3.  \n",
    "def is_consonant(x):\n",
    "    if x not in 'aeiou':\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "        \n",
    "is_consonant('x')\n",
    "is_consonant('l')\n",
    "is_consonant('u')\n",
    "\n",
    "#zach way\n",
    "#is_consonant(character:str)->bool\n",
    "def is_consonant(c):\n",
    "    return c.isaplpha() and not is_vowel(c)\n",
    "is_consonant('a')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Banana\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'Codeup'"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#4. not solved\n",
    "def is_word(x):\n",
    "    if is_vowel == True:\n",
    "        return print('not a consonant')\n",
    "    else:\n",
    "        return print(x.capitalize())\n",
    "is_word('Banana')\n",
    "\n",
    "#capitalizeifconsonant(word:str)->str\n",
    "def capitalize_if_consonant(word):\n",
    "    first_letter = word[0]\n",
    "    if is_consonant(first_letter):\n",
    "        return word.capitalize()\n",
    "    else:\n",
    "        return word\n",
    "capitalize_if_consonant(\"codeup\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "5.  Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "30.0"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#5.  \n",
    "def calculate_tip(tip_percentage, bill_total):\n",
    "    return (bill_total * tip_percentage) \n",
    "calculate_tip(0.20, 20)\n",
    "\n",
    "#calculatetip(percentage: float, bill: float)-> float\n",
    "def calculate_tip(percentage, bill):\n",
    "    tip_amount = percentage * bill\n",
    "    return tip_amount\n",
    "calculate_tip(.15,200)\n",
    "\n",
    "#if someone entered a whole number instead of a percentage\n",
    "#handle the case where a number 1-100 is passed for percentage\n",
    "if percentage > 1:\n",
    "    percentage /= 100\n",
    "tip_amount = percentage * bill\n",
    "return tip_amount\n",
    "\n",
    "def calculate_tip(percentage, bill):\n",
    "    if percentage < 0 or percentage > 1:\n",
    "        raise exception(\"Percentage must be between 0 and 1\")\n",
    "    tip_amount = percentage * bill\n",
    "    return tip_amount"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "6.  Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8.0"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#6.  \n",
    "def apply_discount(original_price, discount_percentage):\n",
    "    return original_price - (original_price * discount_percentage)\n",
    "apply_discount(100, .50)\n",
    "\n",
    "#applydiscount(price:float, discount:float)->float\n",
    "def apply_discount(price, discount):\n",
    "    discount_amount = price * discount\n",
    "    return price - discount_amount\n",
    "apply_discount(10,.20)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1000000.0"
      ]
     },
     "execution_count": 115,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#7. \n",
    "#how to replace in string:  string.replace(oldvalue, newvalue, count)\n",
    "#handlecommas(string)->float\n",
    "def handle_commas(string):\n",
    "    return float(string.replace(\",\", \"\"))\n",
    "\n",
    "handle_commas(\"1,000,000\")\n",
    "    \n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A\n",
      "B\n",
      "F\n"
     ]
    }
   ],
   "source": [
    "#8. getlettergrade(numgrade: float)->str\n",
    "def get_letter_grade(grade):\n",
    "    if grade >= 90:\n",
    "        print('A')\n",
    "    elif grade >= 80:\n",
    "        print('B')\n",
    "    elif grade >= 70:\n",
    "        print('C')\n",
    "    elif grade >= 60:\n",
    "        print('D')\n",
    "    else:\n",
    "        print('F')\n",
    "get_letter_grade(100)\n",
    "get_letter_grade(89)\n",
    "get_letter_grade(34)\n",
    "\n",
    "#Zach way\n",
    "def get_letter_grade(numeric_grade):\n",
    "    if numeric_grade > 90:\n",
    "        return \"A\"\n",
    "    elif numeric_grade > 80:\n",
    "        return \"B\"\n",
    "    elif numeric_grade > 70:\n",
    "        return \"C\"\n",
    "    else:\n",
    "        return \"F\"\n",
    "        \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "remove_vowels called: Processing: abcdef\n",
      "start of for loop. Processing: a\n",
      "end of loop.  new_string: []\n",
      "start of for loop. Processing: b\n",
      "start of loop.  Processing: b\n",
      "end of loop.  new_string: ['b']\n",
      "start of for loop. Processing: c\n",
      "start of loop.  Processing: c\n",
      "end of loop.  new_string: ['b', 'c']\n",
      "start of for loop. Processing: d\n",
      "start of loop.  Processing: d\n",
      "end of loop.  new_string: ['b', 'c', 'd']\n",
      "start of for loop. Processing: e\n",
      "end of loop.  new_string: ['b', 'c', 'd']\n",
      "start of for loop. Processing: f\n",
      "start of loop.  Processing: f\n",
      "end of loop.  new_string: ['b', 'c', 'd', 'f']\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'bcdfg'"
      ]
     },
     "execution_count": 124,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#9. \n",
    "#removevowels(s:string)->string\n",
    "def remove_vowels(string):\n",
    "    #look at each letter in the string\n",
    "    #if its a vowel, it should not be included in the new string\n",
    "    new_string = []\n",
    "    for letter in string:\n",
    "        if not is_vowel(letter):\n",
    "            new_string.append(letter)\n",
    "    return \"\".join(new_string)\n",
    "\n",
    "remove_vowels(\"abcdef\")\n",
    "            \n",
    "\n",
    "#return not inside the loop\n",
    "#return takes whatever is on the right and exits the function\n",
    "#whenever we return inside a loop \n",
    "#return should be at top level of a function\n",
    "#dont want to return inside a loop\n",
    "#function \n",
    "\n",
    "###############################\n",
    "#show how to think about the function\n",
    "#how to get insight into how the code is running\n",
    "#put in print statement for debugging\n",
    "\n",
    "def remove_vowels(string):\n",
    "    new_string = []\n",
    "    print(f\"remove_vowels called: Processing: {string}\")\n",
    "    for character in string:\n",
    "        print(f\"start of for loop. Processing: {character}\")\n",
    "        if not is_vowel(character):\n",
    "            print(f\"start of loop.  Processing: {character}\")\n",
    "            new_string.append(character)\n",
    "        print(f\"end of loop.  new_string: {new_string}\")\n",
    "    return \"\".join(new_string)\n",
    "remove_vowels(\"abcdef\")\n",
    "\n",
    "##short version\n",
    "\n",
    "def remove_vowels(string):\n",
    "    return \"\".join([c for c in string if not is_vowel(c)])\n",
    "\n",
    "remove_vowels(\"abcdefg\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:\n",
    "- anything that is not a valid python identifier should be removed\n",
    "- leading and trailing whitespace should be removed\n",
    "- everything should be lowercase\n",
    "- spaces should be replaced with underscores\n",
    "- for example:\n",
    " - Name will become name\n",
    " - First Name will become first_name\n",
    " - % Completed will become completed"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Removing non whitespace or alnum\n",
      "inside for loop.  Processing F\n",
      "adding F to list...\n",
      " valid_identifier: ['F']\n",
      "inside for loop.  Processing i\n",
      "adding i to list...\n",
      " valid_identifier: ['F', 'i']\n",
      "inside for loop.  Processing r\n",
      "adding r to list...\n",
      " valid_identifier: ['F', 'i', 'r']\n",
      "inside for loop.  Processing s\n",
      "adding s to list...\n",
      " valid_identifier: ['F', 'i', 'r', 's']\n",
      "inside for loop.  Processing t\n",
      "adding t to list...\n",
      " valid_identifier: ['F', 'i', 'r', 's', 't']\n",
      "inside for loop.  Processing  \n",
      "adding   to list...\n",
      " valid_identifier: ['F', 'i', 'r', 's', 't', ' ']\n",
      "inside for loop.  Processing N\n",
      "adding N to list...\n",
      " valid_identifier: ['F', 'i', 'r', 's', 't', ' ', 'N']\n",
      "inside for loop.  Processing a\n",
      "adding a to list...\n",
      " valid_identifier: ['F', 'i', 'r', 's', 't', ' ', 'N', 'a']\n",
      "inside for loop.  Processing m\n",
      "adding m to list...\n",
      " valid_identifier: ['F', 'i', 'r', 's', 't', ' ', 'N', 'a', 'm']\n",
      "inside for loop.  Processing e\n",
      "adding e to list...\n",
      " valid_identifier: ['F', 'i', 'r', 's', 't', ' ', 'N', 'a', 'm', 'e']\n",
      "f i r s t   n a m e\n",
      "f_i_r_s_t___n_a_m_e\n"
     ]
    }
   ],
   "source": [
    "#10 not solved\n",
    "def normalize_name(x):\n",
    "    not_valid_list = []\n",
    "    not_valid = \"!@#$%^&*+=-~`,\"\n",
    "    white_space = \" \"\n",
    "    for identifier in x:\n",
    "        if x in not_valid:\n",
    "            not_valid_list.append(not_valid)\n",
    "    return not_valid_list\n",
    "    \n",
    "normalize_name('!appl!e')\n",
    "\n",
    "#normalizename(s:string)->str\n",
    "def normalize_name(string):\n",
    "    #remove anything thats not whitespace or alphanumeric\n",
    "    valid_identifier = []\n",
    "    print(\"Removing non whitespace or alnum\")\n",
    "    for character in string:\n",
    "        print(f\"inside for loop.  Processing {character}\")\n",
    "        if character.isidentifier() or character == ' ':\n",
    "            print(f\"adding {character} to list...\")\n",
    "            valid_identifier.append(character)\n",
    "        print(f\" valid_identifier: {valid_identifier}\")\n",
    "        #convert valid identifier back to a string\n",
    "    valid_identifier = \" \".join(valid_identifier)\n",
    "    valid_identifier = valid_identifier.lower()\n",
    "    print(valid_identifier)\n",
    "    valid_identifier = valid_identifier.replace(\" \", \"_\")\n",
    "    print(valid_identifier)\n",
    "    \n",
    "normalize_name('First Name')\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.\n",
    "- cumulative_sum([1, 1, 1]) returns [1, 2, 3]\n",
    "- cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "starting out. sums: [1]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[1, 3, 6]"
      ]
     },
     "execution_count": 134,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#11. not solved\n",
    "# cumulativesum(1:list[int])-> list[int]\n",
    "#cumulative_sim([1,1,1]) == [1,2,3]\n",
    "#[1,1+1, 1+2]\n",
    "def cumulative_sum(list_of_numbers):\n",
    "    sums = [list_of_numbers[0]]\n",
    "    print(f\"starting out. sums: {sums}\")\n",
    "    #loop through list of numbers and add to the list as we go\n",
    "    for n in list_of_numbers[1:]:\n",
    "        previous_total = sums[-1]\n",
    "        sums.append(previous_total + n)\n",
    "    return sums\n",
    "        \n",
    "cumulative_sum([1,2,3])\n",
    "####\n",
    "\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "12. Once you've completed the above exercises, follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly comment your code to explain your code."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "13. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#13. not solved\n",
    "def twelveto24(x):\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "14.  Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.\n",
    "- col_index('A') returns 1\n",
    "- col_index('B') returns 2\n",
    "- col_index('AA') returns 27"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#14. not solved"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
