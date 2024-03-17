# Pro Mode Test

_Written by: Jianxing WANG_

_Date: Mar.15_

_Version: 1_

## Single Prediction

#### All legal inputs

| Test         | Description          | Inputs           | Expected Outcome | Test Outcome | Result |
|--------------|----------------------|------------------|------------------|--------------|--------|
| legal inputs | get default teamList | all legal inputs | result page      | result page  | pass   |

#### Test on zipcode

| Test            | Description           | Inputs    | Expected Outcome    | Test Outcome        | Result  |
|-----------------|-----------------------|-----------|---------------------|---------------------|---------|
| long length     | input length over 8   | 123456788 | result page         | result page         | pass    |
| short length    | input length with 1   | 1         | result page         | result page         | pass    |
| decimal         | input decimal         | 1.2345    | input error message | input error message | pass    |
| negative number | input negative number | -12345    | input error message | result page         | fail[1] |

fail[1]: negative number should be considered as illegal input, and showing the input error message when user inputting.

#### Test on latitude

| Test          | Description                      | Inputs       | Expected Outcome    | Test Outcome     | Result  |
|---------------|----------------------------------|--------------|---------------------|------------------|---------|
| long decimal  | input decimal with length over 8 | 40.315315315 | result page         | result page      | pass    |
| over 90       | input nuber that is out of range | 91           | input error message | result page      | fail[2] |
| less than -90 | input nuber that is out of range | -91          | input error message | result page      | fail[3] |
| null          | no input                         | null         | input error message | value error page | fail[4] |

fail[2]&fail[3]: the range of the latitude is between -90 to 90, anything out of that range will be error inputs.

fail[4]: when the latitude value is null, it will return to the value error page, rather than input error message.

#### test on longitude

| Test           | Description                      | Inputs           | Expected Outcome    | Test Outcome | Result  |
|----------------|----------------------------------|------------------|---------------------|--------------|---------|
| long decimal   | input decimal with length over 8 | -74.234232152153 | result page         | result page  | pass    |
| less than -180 | input nuber that is out of range | -181             | input error message | result page  | fail[5] |
| over 180       | input nuber that is out of range | 181              | input error message | result page  | fail[6] |
| null           | no input                         | null             | input error message | error page   | fail[7] |

fail[5]&fail[6]:the range of the longitude is between -180 to 180, anything out of that range will be error inputs.

fail[7]: when the longitude value is null, it will return to the value error page, rather than input error message.

#### test on waterfront

| Test         | Description               | Inputs | Expected Outcome    | Test Outcome        | Result  |
|--------------|---------------------------|--------|---------------------|---------------------|---------|
| out of range | input number except 0 & 1 | 2      | input error message | result page         | fail[8] |
| decimal      | input decimal             | 1.2    | input error message | input error message | pass    |
| null         | no input                  | null   | input error message | error page          | fail[9] |

fail[8]: the input except 0 & 1 will also be recorded as valid inputs.

fail[9]: when the waterfront value is null, it will return to the value error page, rather than input error message.

#### test on bedrooms number

| Test            | Description           | Inputs | Expected Outcome    | Test Outcome        | Result   |
|-----------------|-----------------------|--------|---------------------|---------------------|----------|
| decimal         | input decimal         | 2.5    | input error message | input error message | pass     |
| negative number | input negative number | -2     | input error message | result page         | fail[10] |
| null            | no input              | null   | input error message | error page          | fail[11] |

fail[10]: the negative number of the bedrooms number should be illegal input.

fail[11]: when the bedroom value is null, it will return to the value error page, rather than input error message.

#### test on bathrooms number

| Test            | Description           | Inputs | Expected Outcome    | Test Outcome        | Result   |
|-----------------|-----------------------|--------|---------------------|---------------------|----------|
| decimal         | input decimal         | 2.5    | input error message | input error message | pass     |
| negative number | input negative number | -2     | input error message | result page         | fail[12] |
| null            | no input              | null   | input error message | error page          | fail[13] |

fail[12]: the negative number of the bathrooms number should be illegal input.

fail[13]: when the bathroom value is null, it will return to the value error page, rather than input error message.

#### test on floors number

| Test            | Description           | Inputs | Expected Outcome    | Test Outcome        | Result   |
|-----------------|-----------------------|--------|---------------------|---------------------|----------|
| decimal         | input decimal         | 2.5    | input error message | input error message | pass     |
| negative number | input negative number | -2     | input error message | result page         | fail[14] |
| null            | no input              | null   | input error message | error page          | fail[15] |

fail[14]: the negative number of the floors number should be illegal input.

fail[15]: when the floors value is null, it will return to the value error page, rather than input error message.

#### test on build year

| Test            | Description           | Inputs | Expected Outcome    | Test Outcome        | Result   |
|-----------------|-----------------------|--------|---------------------|---------------------|----------|
| decimal         | input decimal         | 2010.2 | input error message | input error message | pass     |
| negative number | input negative number | -2010  | input error message | result page         | fail[16] |
| null            | no input              | null   | input error message | error page          | fail[17] |

fail[16]: the number of year should not be negative number.

fail[17]: when the year value is null, it will return to the value error page, rather than input error message.

#### test on Renovated year

| Test                    | Description                               | Inputs | Expected Outcome    | Test Outcome        | Result   |
|-------------------------|-------------------------------------------|--------|---------------------|---------------------|----------|
| decimal                 | input decimal                             | 2018.2 | input error message | input error message | pass     |
| negative number         | input negative number                     | -2018  | input error message | result page         | fail[18] |
| earlier than build year | input number that is less than build year | 2008   | input error message | result page         | fail[19] |
| null                    | no input                                  | null   | input error message | error page          | fail[20] |

fail[18]: the number of year should not be negative number.

fail[19]: the number of renovated year should be less than build year.

fail[20]: when the year value is null, it will return to the value error page, rather than input error message.

#### test on living space

| Test            | Description           | Inputs | Expected Outcome    | Test Outcome        | Result   |
|-----------------|-----------------------|--------|---------------------|---------------------|----------|
| decimal         | input decimal         | 235.2  | input error message | input error message | pass     |
| negative number | input negative number | -235   | input error message | result page         | fail[21] |
| null            | no input              | null   | input error message | error page          | fail[22] |

fail[21]: the number of living space should not be negative number, it should return error message.

fail[22]: when the space value is null, it will return to the value error page, rather than input error message.

#### test on lot space

| Test            | Description           | Inputs | Expected Outcome    | Test Outcome        | Result   |
|-----------------|-----------------------|--------|---------------------|---------------------|----------|
| decimal         | input decimal         | 234.2  | input error message | input error message | pass     |
| negative number | input negative number | -234   | input error message | result page         | fail[23] |
| null            | no input              | null   | input error message | error page          | fail[24] |

fail[23]: the number of lot space should not be negative number, it should return error message.

fail[24]: when the space value is null, it will return to the value error page, rather than input error message.

#### test on above basement space

| Test            | Description           | Inputs | Expected Outcome    | Test Outcome        | Result   |
|-----------------|-----------------------|--------|---------------------|---------------------|----------|
| decimal         | input decimal         | 32.2   | input error message | input error message | pass     |
| negative number | input negative number | -32    | input error message | result page         | fail[25] |
| null            | no input              | null   | input error message | error page          | fail[26] |

fail[25]: the number of above basement space should not be negative number, it should return error message.

fail[26]: when the space value is null, it will return to the value error page, rather than input error message.

#### test on basement space

| Test            | Description           | Inputs | Expected Outcome    | Test Outcome        | Result   |
|-----------------|-----------------------|--------|---------------------|---------------------|----------|
| decimal         | input decimal         | 23.2   | input error message | input error message | pass     |
| negative number | input negative number | -23    | input error message | result page         | fail[27] |
| null            | no input              | null   | input error message | error page          | fail[28] |

fail[27]: the number of basement space should not be negative number, it should return error message.

fail[28]: when the space value is null, it will return to the value error page, rather than input error message.

#### test on view number

| Test            | Description           | Inputs | Expected Outcome    | Test Outcome        | Result   |
|-----------------|-----------------------|--------|---------------------|---------------------|----------|
| decimal         | input decimal         | 2.2    | input error message | input error message | pass     |
| negative number | input negative number | -2     | input error message | result page         | fail[29] |
| null            | no input              | null   | input error message | error page          | fail[30] |

fail[29]: the number of view number should not be negative number, it should return error message.

fail[30]: when the view value is null, it will return to the value error page, rather than input error message.

#### test on condition

| Test            | Description           | Inputs | Expected Outcome    | Test Outcome        | Result   |
|-----------------|-----------------------|--------|---------------------|---------------------|----------|
| decimal         | input decimal         | 4.5    | input error message | input error message | pass     |
| negative number | input negative number | -4     | input error message | result page         | fail[31] |
| null            | no input              | null   | input error message | error page          | fail[32] |

fail[31]: the number of view number should not be negative number, it should return error message.

fail[32]: when the condition value is null, it will return to the value error page, rather than input error message.

#### test on grade

| Test            | Description           | Inputs | Expected Outcome    | Test Outcome        | Result   |
|-----------------|-----------------------|--------|---------------------|---------------------|----------|
| decimal         | input decimal         | 6.5    | input error message | input error message | pass     |
| negative number | input negative number | -6     | input error message | result page         | fail[33] |
| null            | no input              | null   | input error message | error page          | fail[34] |

fail[33]: the number of view number should not be negative number, it should return error message.

fail[34]: when the grade value is null, it will return to the value error page, rather than input error message.

#### test on living space in 2015

| Test            | Description           | Inputs | Expected Outcome    | Test Outcome        | Result   |
|-----------------|-----------------------|--------|---------------------|---------------------|----------|
| decimal         | input decimal         | 235.5  | input error message | input error message | pass     |
| negative number | input negative number | -235   | input error message | result page         | fail[35] |
| null            | no input              | null   | input error message | error page          | fail[36] |

fail[35]: the number of living space should not be negative number, it should return error message.

fail[36]: when the space is null, it will return to the value error page, rather than input error message.

#### test on lot space in 2015

| Test            | Description           | Inputs | Expected Outcome    | Test Outcome        | Result   |
|-----------------|-----------------------|--------|---------------------|---------------------|----------|
| decimal         | input decimal         | 234.5  | input error message | input error message | pass     |
| negative number | input negative number | -234   | input error message | result page         | fail[37] |
| null            | no input              | null   | input error message | error page          | fail[38] |

fail[37]: the number of lot space should not be negative number, it should return error message.

fail[38]: when the space is null, it will return to the value error page, rather than input error message.

