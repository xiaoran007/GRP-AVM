# Pro Mode Test

_Written by: Jianxing WANG_

_Date: Mar.16_

_Version: 2_

## Single Prediction

#### All legal inputs

| bedrooms | bathrooms | sqft_living | sqft_lot | floors | waterfront | view | condition | grade | sqft_above | sqft_basement | yr_built | yr_renovated | zipcode | lat     | long     | sqft_living15 | sqft_lot15 |
|----------|-----------|-------------|----------|--------|------------|------|-----------|-------|------------|---------------|----------|--------------|---------|---------|----------|---------------|------------|
| 3        | 1         | 1180        | 5650     | 1      | 0          | 0    | 3         | 7     | 1180       | 0             | 1955     | 0            | 98178   | 47.5112 | -122.257 | 1340          | 5650       |

| Test         | Description            | Inputs           | Expected Outcome | Test Outcome | Result |
|--------------|------------------------|------------------|------------------|--------------|--------|
| legal inputs | input the legal inputs | all legal inputs | result page      | result page  | pass   |

#### Test on zipcode

| Test            | Description           | Inputs    | Expected Outcome    | Test Outcome        | Result |
|-----------------|-----------------------|-----------|---------------------|---------------------|--------|
| long length     | input length over 8   | 123456788 | result page         | result page         | pass   |
| short length    | input length with 1   | 1         | result page         | result page         | pass   |
| decimal         | input decimal         | 1.2345    | input error message | input error message | pass   |
| negative number | input negative number | -98178    | input error message | input error message | pass   |

#### Test on latitude

| Test          | Description                      | Inputs       | Expected Outcome    | Test Outcome        | Result |
|---------------|----------------------------------|--------------|---------------------|---------------------|--------|
| long decimal  | input decimal with length over 8 | 40.315315315 | result page         | result page         | pass   |
| over 90       | input nuber that is out of range | 91           | input error message | input error message | pass   |
| less than -90 | input nuber that is out of range | -91          | input error message | input error message | pass   |
| null          | no input                         | null         | input error message | input error message | pass   |

#### Test on longitude

| Test           | Description                      | Inputs           | Expected Outcome    | Test Outcome        | Result |
|----------------|----------------------------------|------------------|---------------------|---------------------|--------|
| long decimal   | input decimal with length over 8 | -74.234232152153 | result page         | result page         | pass   |
| less than -180 | input nuber that is out of range | -181             | input error message | input error message | pass   |
| over 180       | input nuber that is out of range | 181              | input error message | input error message | pass   |
| null           | no input                         | null             | input error message | input error message | pass   |

#### Test on waterfront

| Test         | Description               | Inputs | Expected Outcome    | Test Outcome        | Result |
|--------------|---------------------------|--------|---------------------|---------------------|--------|
| out of range | input number except 0 & 1 | 2      | input error message | input error message | pass   |
| decimal      | input decimal             | 1.2    | input error message | input error message | pass   |
| null         | no input                  | null   | input error message | input error message | pass   |

#### Test on bedrooms number

| Test            | Description           | Inputs | Expected Outcome    | Test Outcome        | Result |
|-----------------|-----------------------|--------|---------------------|---------------------|--------|
| decimal         | input decimal         | 2.5    | input error message | input error message | pass   |
| negative number | input negative number | -2     | input error message | input error message | pass   |
| null            | no input              | null   | input error message | input error message | pass   |

#### Test on bathrooms number

| Test            | Description           | Inputs | Expected Outcome    | Test Outcome        | Result |
|-----------------|-----------------------|--------|---------------------|---------------------|--------|
| decimal         | input decimal         | 2.5    | input error message | input error message | pass   |
| negative number | input negative number | -2     | input error message | input error message | pass   |
| null            | no input              | null   | input error message | input error message | pass   |

#### Test on floors number

| Test            | Description           | Inputs | Expected Outcome    | Test Outcome        | Result |
|-----------------|-----------------------|--------|---------------------|---------------------|--------|
| decimal         | input decimal         | 2.5    | input error message | input error message | pass   |
| negative number | input negative number | -2     | input error message | input error message | pass   |
| null            | no input              | null   | input error message | input error message | pass   |

#### Test on build year

| Test            | Description           | Inputs | Expected Outcome    | Test Outcome        | Result |
|-----------------|-----------------------|--------|---------------------|---------------------|--------|
| decimal         | input decimal         | 2010.2 | input error message | input error message | pass   |
| negative number | input negative number | -2010  | input error message | input error message | pass   |
| null            | no input              | null   | input error message | input error message | pass   |

#### Test on Renovated year

| Test                    | Description                               | Inputs | Expected Outcome    | Test Outcome        | Result |
|-------------------------|-------------------------------------------|--------|---------------------|---------------------|--------|
| decimal                 | input decimal                             | 2018.2 | input error message | input error message | pass   |
| negative number         | input negative number                     | -2018  | input error message | input error message | pass   |
| earlier than build year | input number that is less than build year | 2008   | input error message | input error message | pass   |
| null                    | no input                                  | null   | input error message | input error message | pass   |

#### Test on living space

| Test            | Description           | Inputs | Expected Outcome    | Test Outcome        | Result |
|-----------------|-----------------------|--------|---------------------|---------------------|--------|
| decimal         | input decimal         | 1180.2 | input error message | input error message | pass   |
| negative number | input negative number | -1180  | input error message | input error message | pass   |
| null            | no input              | null   | input error message | input error message | pass   |

#### Test on lot space

| Test            | Description           | Inputs | Expected Outcome    | Test Outcome        | Result |
|-----------------|-----------------------|--------|---------------------|---------------------|--------|
| decimal         | input decimal         | 5650.2 | input error message | input error message | pass   |
| negative number | input negative number | -5650  | input error message | input error message | pass   |
| null            | no input              | null   | input error message | input error message | pass   |

#### Test on above basement space

| Test            | Description           | Inputs | Expected Outcome    | Test Outcome        | Result |
|-----------------|-----------------------|--------|---------------------|---------------------|--------|
| decimal         | input decimal         | 32.2   | input error message | input error message | pass   |
| negative number | input negative number | -32    | input error message | input error message | pass   |
| null            | no input              | null   | input error message | input error message | pass   |

#### Test on basement space

| Test            | Description           | Inputs | Expected Outcome    | Test Outcome        | Result |
|-----------------|-----------------------|--------|---------------------|---------------------|--------|
| decimal         | input decimal         | 400.2  | input error message | input error message | pass   |
| negative number | input negative number | -400   | input error message | input error message | pass   |
| null            | no input              | null   | input error message | input error message | pass   |

#### Test on view number

| Test            | Description           | Inputs | Expected Outcome    | Test Outcome        | Result |
|-----------------|-----------------------|--------|---------------------|---------------------|--------|
| decimal         | input decimal         | 2.2    | input error message | input error message | pass   |
| negative number | input negative number | -2     | input error message | input error message | pass   |
| null            | no input              | null   | input error message | input error message | pass   |

#### Test on condition

| Test            | Description                                  | Inputs | Expected Outcome    | Test Outcome        | Result |
|-----------------|----------------------------------------------|--------|---------------------|---------------------|--------|
| decimal         | input decimal                                | 4.5    | input error message | input error message | pass   |
| negative number | input negative number                        | -4     | input error message | result page         | pass   |
| null            | no input                                     | null   | input error message | error page          | pass   |
| out of range    | input the number outside the range of 0 to 5 | 6      | input error message | input error message | pass   | 

#### Test on grade

| Test            | Description                                   | Inputs | Expected Outcome    | Test Outcome        | Result |
|-----------------|-----------------------------------------------|--------|---------------------|---------------------|--------|
| decimal         | input decimal                                 | 6.5    | input error message | input error message | pass   |
| negative number | input negative number                         | -6     | input error message | input error message | pass   |
| null            | no input                                      | null   | input error message | input error message | pass   |
| out of range    | input the number outside the range of 1 to 13 | 20     | input error message | input error message | pass   | 

#### Test on living space in 2015

| Test            | Description           | Inputs | Expected Outcome    | Test Outcome        | Result |
|-----------------|-----------------------|--------|---------------------|---------------------|--------|
| decimal         | input decimal         | 1340.5 | input error message | input error message | pass   |
| negative number | input negative number | -1340  | input error message | input error message | pass   |
| null            | no input              | null   | input error message | input error message | pass   |

#### Test on lot space in 2015

| Test            | Description           | Inputs | Expected Outcome    | Test Outcome        | Result |
|-----------------|-----------------------|--------|---------------------|---------------------|--------|
| decimal         | input decimal         | 5650.5 | input error message | input error message | pass   |
| negative number | input negative number | -5650  | input error message | input error message | pass   |
| null            | no input              | null   | input error message | input error message | pass   |

#### Test on confidence level

| Test            | Description                                  | Inputs | Expected Outcome    | Test Outcome        | Result |
|-----------------|----------------------------------------------|--------|---------------------|---------------------|--------|
| decimal         | input decimal                                | .7     | result page         | result page         | pass   |
| negative number | input negative number                        | -0.7   | input error message | input error message | pass   |
| null            | no input                                     | null   | input error message | input error message | pass   |
| out of range    | input the number outside the range of 0 to 1 | 1      | input error message | input error message | pass   | 

#### Test on Pro settings

| Test                              | Description                          | Inputs | Expected Outcome                               | Test Outcome                                   | Result |
|-----------------------------------|--------------------------------------|--------|------------------------------------------------|------------------------------------------------|--------|
| enable LLM                        | choose LLM                           | chosen | result page with LLM                           | result page with LLM                           | pass   |
| enable full prediction            | choose full prediction               | chosen | result page with full prediction               | result page with full prediction               | pass   |
| use user-defined confidence level | choose user-defined confidence level | chosen | result page with user-defined confidence level | result page with user-defined confidence level | pass   |
| enable hidden prediction          | choose hidden prediction             | chosen | result page with no ID                         | result page with no ID                         | pass   | 

#### Test on models

| Test     | Description                                     | Inputs   | Expected Outcome            | Test Outcome                | Result |
|----------|-------------------------------------------------|----------|-----------------------------|-----------------------------|--------|
| null     | user didn't choose model (use default mode: RF) | null     | result page with RF model   | result page with RF model   | pass   |
| XGBoost  | select XGB model                                | XGBoost  | result page with XGB model  | result page with XGB model  | pass   |
| LightGBM | select LGBM model                               | LightGBM | result page with LGBM model | result page with LGBM model | pass   |

## Historical Prediction

Assume there's a result ID: 593306

#### Test on Result ID

| Test                | Description                                | Inputs  | Expected Outcome                | Test Outcome                    | Result |
|---------------------|--------------------------------------------|---------|---------------------------------|---------------------------------|--------|
| valid ID            | input valid ID number that already exist   | 593306  | result page with ID: 593306     | result page with ID: 593306     | pass   |
| decimal             | input decimal                              | 5.93306 | input error message             | input error message             | pass   |
| negative            | input negative number                      | -593306 | Corresponding records not found | Corresponding records not found | pass   |
| not recorded number | input the number that have not been record | 123456  | Corresponding records not found | Corresponding records not found | pass   |

## Batch Prediction

#### Test on models

| Test     | Description                                     | Inputs   | Expected Outcome            | Test Outcome                | Result |
|----------|-------------------------------------------------|----------|-----------------------------|-----------------------------|--------|
| null     | user didn't choose model (use default mode: RF) | null     | result page with RF model   | result page with RF model   | pass   |
| XGBoost  | select XGB model                                | XGBoost  | result page with XGB model  | result page with XGB model  | pass   |
| LightGBM | select LGBM model                               | LightGBM | result page with LGBM model | result page with LGBM model | pass   |

#### Test file uploaded

| Test              | Description              | Inputs            | Expected Outcome | Test Outcome | Result |
|-------------------|--------------------------|-------------------|------------------|--------------|--------|
| csv file          | upload csv file          | csv file          | result page      | result page  | pass   |
| other format file | upload other format file | other format file | error page       | error page   | pass   |
| null              | no file is chosen        | null              | error page       | error page   | pass   |

## Result Page

#### Test download

| Test          | Description   | Inputs                | Expected Outcome   | Test Outcome       | Result |
|---------------|---------------|-----------------------|--------------------|--------------------|--------|
| download file | download file | click download button | file is downloaded | file is downloaded | pass   |
