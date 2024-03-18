# Normal Mode Test

_Written by: Panfeng HU_

_Date: Mar.18_

_Version: 1_

## Single Prediction

#### All legal inputs

| Test         | Description          | Inputs           | Expected Outcome | Test Outcome | Result |
|--------------|----------------------|------------------|------------------|--------------|--------|
| legal inputs | get default teamList | all legal inputs | result page      | result page  | pass   |

#### Test on zipcode

| Test            | Description           | Inputs   | Expected Outcome   | Test Outcome            | Result |
|-----------------|-----------------------|----------|--------------------|-------------------------|--------|
| long length     | input length over 8   | 99999999 | result page        | result page             | pass   |
| short length    | input length with 1   | 1        | result page        | result page             | pass   |
| decimal         | input decimal         | 1.2345   | input error prompt | input error prompt      | pass   |
| negative number | input negative number | -1       | input error prompt | input error prompt page | pass   |

#### Test on latitude

| Test          | Description                      | Inputs       | Expected Outcome   | Test Outcome       | Result |
|---------------|----------------------------------|--------------|--------------------|--------------------|--------|
| long decimal  | input decimal with length over 8 | 47.511277777 | result page        | result page        | pass   |
| over 90       | input nuber that is out of range | 91           | input error prompt | input error prompt | pass   |
| less than -90 | input nuber that is out of range | -91          | input error prompt | input error prompt | pass   |
| null          | no input                         | null         | input error prompt | input error prompt | pass   |

#### test on longitude

| Test           | Description                      | Inputs             | Expected Outcome   | Test Outcome       | Result |
|----------------|----------------------------------|--------------------|--------------------|--------------------|--------|
| long decimal   | input decimal with length over 8 | -122.2577777777777 | result page        | result page        | pass   |
| less than -180 | input nuber that is out of range | -181               | input error prompt | input error prompt | pass   |
| over 180       | input nuber that is out of range | 181                | input error prompt | input error prompt | pass   |
| null           | no input                         | null               | input error prompt | input error prompt | pass   |

#### test on waterfront

| Test       | Description     | Inputs | Expected Outcome | Test Outcome | Result |
|------------|-----------------|--------|------------------|--------------|--------|
| choose yes | click input yes | yes    | result page      | result page  | pass   |
| choose no  | click input no  | no     | result page      | result page  | pass   |

`#### test on bedrooms number

| Test            | Description           | Inputs | Expected Outcome   | Test Outcome            | Result |
|-----------------|-----------------------|--------|--------------------|-------------------------|--------|
| decimal         | input decimal         | 2.3    | input error prompt | input error prompt      | pass   |
| negative number | input negative number | -2     | input error prompt | input error prompt page | pass   |
| null            | no input              | null   | input error prompt | input error prompt      | pass   |

#### test on bathrooms number

| Test            | Description           | Inputs | Expected Outcome   | Test Outcome       | Result |
|-----------------|-----------------------|--------|--------------------|--------------------|--------|
| decimal         | input decimal         | 2.5    | result page        | result page        | pass   |
| negative number | input negative number | -2     | input error prompt | input error prompt | pass   |
| null            | no input              | null   | input error prompt | input error prompt | pass   |

#### test on floors number

| Test            | Description           | Inputs | Expected Outcome   | Test Outcome       | Result |
|-----------------|-----------------------|--------|--------------------|--------------------|--------|
| decimal         | input decimal         | 2.5    | result page        | result page        | pass   |
| negative number | input negative number | -2     | input error prompt | input error prompt | pass   |
| null            | no input              | null   | input error prompt | input error prompt | pass   |

#### test on build year

| Test            | Description           | Inputs | Expected Outcome   | Test Outcome       | Result |
|-----------------|-----------------------|--------|--------------------|--------------------|--------|
| decimal         | input decimal         | 2010.2 | input error prompt | input error prompt | pass   |
| negative number | input negative number | -2010  | input error prompt | input error prompt | pass   |
| null            | no input              | null   | input error prompt | input error prompt | pass   |

#### test on Renovated year

| Test                    | Description                               | Inputs | Expected Outcome   | Test Outcome       | Result |
|-------------------------|-------------------------------------------|--------|--------------------|--------------------|--------|
| decimal                 | input decimal                             | 2018.2 | input error prompt | input error prompt | pass   |
| negative number         | input negative number                     | -2018  | input error prompt | input error prompt | pass   |
| earlier than build year | input number that is less than build year | 2008   | input error prompt | input error prompt | pass   |
| null                    | no input                                  | null   | input error prompt | input error prompt | pass   |

#### test on living size

| Test            | Description           | Inputs | Expected Outcome   | Test Outcome       | Result |
|-----------------|-----------------------|--------|--------------------|--------------------|--------|
| decimal         | input decimal         | 235.2  | result page        | result page        | pass   |
| negative number | input negative number | -235   | input error prompt | input error prompt | pass   |
| null            | no input              | null   | input error prompt | input error prompt | pass   |

#### test on lot size

| Test            | Description           | Inputs | Expected Outcome   | Test Outcome       | Result |
|-----------------|-----------------------|--------|--------------------|--------------------|--------|
| decimal         | input decimal         | 234.2  | result page        | result page        | pass   |
| negative number | input negative number | -234   | input error prompt | input error prompt | pass   |
| null            | no input              | null   | input error prompt | input error prompt | pass   |

#### test on above basement size

| Test            | Description           | Inputs | Expected Outcome   | Test Outcome | Result |
|-----------------|-----------------------|--------|--------------------|--------------|--------|
| decimal         | input decimal         | 32.2   | result page        | result page  | pass   |
| negative number | input negative number | -32    | input error prompt | result page  | pass   |
| null            | no input              | null   | input error prompt | error page   | pass   |

#### test on basement size

| Test            | Description           | Inputs | Expected Outcome   | Test Outcome       | Result |
|-----------------|-----------------------|--------|--------------------|--------------------|--------|
| decimal         | input decimal         | 23.2   | result page        | result page        | pass   |
| negative number | input negative number | -23    | input error prompt | input error prompt | pass   |
| null            | no input              | null   | input error prompt | input error prompt | pass   |

#### test on view number

| Test            | Description           | Inputs | Expected Outcome   | Test Outcome       | Result |
|-----------------|-----------------------|--------|--------------------|--------------------|--------|
| decimal         | input decimal         | 2.2    | input error prompt | input error prompt | pass   |
| negative number | input negative number | -2     | input error prompt | input error prompt | pass   |
| null            | no input              | null   | input error prompt | input error prompt | pass   |

#### test on condition

| Test                        | Description          | Inputs         | Expected Outcome   | Test Outcome | Result   |
|-----------------------------|----------------------|----------------|--------------------|--------------|----------|
| choose more than one button | click all the button | all the button | input error prompt | error page   | fault[1] |

fault[1]：user could choose more than one button,when submit the form,the system will return the error page.

#### test on grade

| Test            | Description           | Inputs | Expected Outcome   | Test Outcome       | Result |
|-----------------|-----------------------|--------|--------------------|--------------------|--------|
| decimal         | input decimal         | 6.5    | input error prompt | input error prompt | pass   |
| negative number | input negative number | -6     | input error prompt | input error prompt | pass   |
| null            | no input              | null   | input error prompt | input error prompt | pass   |

#### test on living size in 2015

| Test            | Description           | Inputs | Expected Outcome   | Test Outcome       | Result |
|-----------------|-----------------------|--------|--------------------|--------------------|--------|
| decimal         | input decimal         | 235.5  | result page        | result page        | pass   |
| negative number | input negative number | -235   | input error prompt | input error prompt | pass   |
| null            | no input              | null   | input error prompt | input error prompt | pass   |

#### test on lot size in 2015

| Test            | Description           | Inputs | Expected Outcome   | Test Outcome       | Result |
|-----------------|-----------------------|--------|--------------------|--------------------|--------|
| decimal         | input decimal         | 234.5  | result page        | result page        | pass   |
| negative number | input negative number | -234   | input error prompt | input error prompt | pass   |
| null            | no input              | null   | input error prompt | input error prompt | pass   |


