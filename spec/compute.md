# COMPUTE transformations

| name          | dense only operation   | logical operation   | pybids implemented   | bids-matlab implemented   |
|:--------------|:-----------------------|:--------------------|:---------------------|:--------------------------|
| Add           | False                  | False               | False                | True                      |
| And           | False                  | True                | True                 | True                      |
| Constant      | False                  | False               | False                | True                      |
| Convolve      | True                   | False               | True                 | False                     |
| Deconvolve    | True                   | False               | False                | False                     |
| Demean        | False                  | False               | True                 | False                     |
| Derivative    | False                  | False               | False                | False                     |
| Divide        | False                  | False               | False                | True                      |
| Lag           | True                   | False               | True                 | False                     |
| Mean          | False                  | False               | False                | True                      |
| Multiply      | False                  | False               | False                | True                      |
| Not           | False                  | True                | True                 | True                      |
| Or            | False                  | True                | True                 | True                      |
| Orthogonalize | False                  | False               | True                 | False                     |
| PCA           | True                   | False               | False                | False                     |
| Power         | False                  | False               | False                | True                      |
| Product       | False                  | False               | True                 | True                      |
| Scale         | False                  | False               | True                 | True                      |
| StdDev        | False                  | False               | False                | True                      |
| Subtract      | False                  | False               | False                | True                      |
| Sum           | False                  | False               | True                 | True                      |
| Threshold     | False                  | False               | True                 | True                      |
| Variance      | False                  | False               | False                | False                     |


## Constant with value

### input

|   onset |   duration | trial_type   |   to_threshold |
|--------:|-----------:|:-------------|---------------:|
|       2 |          2 | VisMot       |              1 |
|       4 |          2 | VisStat      |              2 |
|       6 |          2 | VisMot       |             -1 |
|       8 |          2 | VisStat      |             -2 |

### transformation 

```json
{
    "Description": "Constantwithvalue",
    "Instruction": {
        "Name": "Constant",
        "Value": 2,
        "Output": "cst"
    }
}
```

### output 

|   onset |   duration | trial_type   |   to_threshold |   cst |
|--------:|-----------:|:-------------|---------------:|------:|
|       2 |          2 | VisMot       |              1 |     2 |
|       4 |          2 | VisStat      |              2 |     2 |
|       6 |          2 | VisMot       |             -1 |     2 |
|       8 |          2 | VisStat      |             -2 |     2 |


## Add coerce value

### input

|   onset |   duration | trial_type   |   intensity |
|--------:|-----------:|:-------------|------------:|
|       2 |          2 | VisMot       |           2 |
|       4 |          2 | VisStat      |          -4 |

### transformation 

```json
{
    "Description": "Addcoercevalue",
    "Instruction": {
        "Name": "Add",
        "Input": "onset",
        "Value": "3"
    }
}
```

### output 

|   onset |   duration | trial_type   |   intensity |
|--------:|-----------:|:-------------|------------:|
|       5 |          2 | VisMot       |           2 |
|       7 |          2 | VisStat      |          -4 |


## Add to specific rows

### input

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|
|       2 |          2 |            1 | Famous face     | Face         |            1.5  |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |
|       5 |          2 |            2 | Famous face     | Face         |            1.56 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |

### transformation 

```json
{
    "Description": "Addtospecificrows",
    "Instruction": {
        "Name": "Add",
        "Input": "onset",
        "Query": "familiarity == Famous face",
        "Value": 3
    }
}
```

### output 

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|
|       5 |          2 |            1 | Famous face     | Face         |            1.5  |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |
|       8 |          2 |            2 | Famous face     | Face         |            1.56 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |


## Sum

### input

|   onset |   duration | trial_type   |   to_threshold |
|--------:|-----------:|:-------------|---------------:|
|       2 |          2 | VisMot       |              1 |
|       4 |          2 | VisStat      |              2 |
|       6 |          2 | VisMot       |             -1 |
|       8 |          2 | VisStat      |             -2 |

### transformation 

```json
{
    "Description": "Sum",
    "Instruction": {
        "Name": "Sum",
        "Input": [
            "onset",
            "duration"
        ],
        "Output": "onset_plus_duration"
    }
}
```

### output 

|   onset |   duration | trial_type   |   to_threshold |   onset_plus_duration |
|--------:|-----------:|:-------------|---------------:|----------------------:|
|       2 |          2 | VisMot       |              1 |                     4 |
|       4 |          2 | VisStat      |              2 |                     6 |
|       6 |          2 | VisMot       |             -1 |                     8 |
|       8 |          2 | VisStat      |             -2 |                    10 |


## Scale all options

### input

|   sex_m | handedness   | sex   |   age_gt_twenty |   age |
|--------:|:-------------|:------|----------------:|------:|
|       1 | right        | M     |               1 |    21 |
|       1 | left         | M     |               0 |    18 |
|       0 | nan          | F     |               1 |    46 |
|       0 | left         | F     |               0 |    10 |
|       0 | right        | F     |               0 |   nan |

### transformation 

```json
{
    "Description": "Scalealloptions",
    "Instruction": {
        "Name": "Scale",
        "Input": [
            "age"
        ],
        "Demean": true,
        "Rescale": true,
        "ReplaceNa": "off",
        "Output": [
            "age_demeaned_centered"
        ]
    }
}
```

### output 

|   sex_m | handedness   | sex   |   age_gt_twenty |   age |   age_demeaned_centered |
|--------:|:-------------|:------|----------------:|------:|------------------------:|
|       1 | right        | M     |               1 |    21 |               -0.176929 |
|       1 | left         | M     |               0 |    18 |               -0.369943 |
|       0 | nan          | F     |               1 |    46 |                1.43152  |
|       0 | left         | F     |               0 |    10 |               -0.884645 |
|       0 | right        | F     |               0 |   nan |              nan        |


## Constant basic

### input

|   onset |   duration | trial_type   |   to_threshold |
|--------:|-----------:|:-------------|---------------:|
|       2 |          2 | VisMot       |              1 |
|       4 |          2 | VisStat      |              2 |
|       6 |          2 | VisMot       |             -1 |
|       8 |          2 | VisStat      |             -2 |

### transformation 

```json
{
    "Description": "Constantbasic",
    "Instruction": {
        "Name": "Constant",
        "Output": "cst"
    }
}
```

### output 

|   onset |   duration | trial_type   |   to_threshold |   cst |
|--------:|-----------:|:-------------|---------------:|------:|
|       2 |          2 | VisMot       |              1 |     1 |
|       4 |          2 | VisStat      |              2 |     1 |
|       6 |          2 | VisMot       |             -1 |     1 |
|       8 |          2 | VisStat      |             -2 |     1 |


## Threshold binarize above singed

### input

|   onset |   duration | trial_type   |   to_threshold |
|--------:|-----------:|:-------------|---------------:|
|       2 |          2 | VisMot       |              1 |
|       4 |          2 | VisStat      |              2 |
|       6 |          2 | VisMot       |             -1 |
|       8 |          2 | VisStat      |             -2 |

### transformation 

```json
{
    "Description": "Thresholdbinarizeabovesinged",
    "Instruction": {
        "Name": "Threshold",
        "Input": "to_threshold",
        "Threshold": 1,
        "Binarize": true,
        "Above": true,
        "Signed": false
    }
}
```

### output 

|   onset |   duration | trial_type   |   to_threshold |
|--------:|-----------:|:-------------|---------------:|
|       2 |          2 | VisMot       |              0 |
|       4 |          2 | VisStat      |              1 |
|       6 |          2 | VisMot       |              0 |
|       8 |          2 | VisStat      |              1 |


## Scale

### input

|   sex_m | handedness   | sex   |   age_gt_twenty |   age |
|--------:|:-------------|:------|----------------:|------:|
|       1 | right        | M     |               1 |    21 |
|       1 | left         | M     |               0 |    18 |
|       0 | nan          | F     |               1 |    46 |
|       0 | left         | F     |               0 |    10 |
|       0 | right        | F     |               0 |   nan |

### transformation 

```json
{
    "Description": "Scale",
    "Instruction": {
        "Name": "Scale",
        "Input": [
            "age"
        ]
    }
}
```

### output 

|   sex_m | handedness   | sex   |   age_gt_twenty |        age |
|--------:|:-------------|:------|----------------:|-----------:|
|       1 | right        | M     |               1 |  -0.176929 |
|       1 | left         | M     |               0 |  -0.369943 |
|       0 | nan          | F     |               1 |   1.43152  |
|       0 | left         | F     |               0 |  -0.884645 |
|       0 | right        | F     |               0 | nan        |


## Power

### input

|   onset |   duration | trial_type   |   intensity |
|--------:|-----------:|:-------------|------------:|
|       2 |          2 | VisMot       |           2 |
|       4 |          2 | VisStat      |          -4 |

### transformation 

```json
{
    "Description": "Power",
    "Instruction": {
        "Name": "Power",
        "Input": "intensity",
        "Value": 2
    }
}
```

### output 

|   onset |   duration | trial_type   |   intensity |
|--------:|-----------:|:-------------|------------:|
|       2 |          2 | VisMot       |           4 |
|       4 |          2 | VisStat      |          16 |


## Power with output

### input

|   onset |   duration | trial_type   |   intensity |
|--------:|-----------:|:-------------|------------:|
|       2 |          2 | VisMot       |           2 |
|       4 |          2 | VisStat      |          -4 |

### transformation 

```json
{
    "Description": "Powerwithoutput",
    "Instruction": {
        "Name": "Power",
        "Input": "intensity",
        "Value": 3,
        "Output": "intensity_cubed"
    }
}
```

### output 

|   onset |   duration | trial_type   |   intensity |   intensity_cubed |
|--------:|-----------:|:-------------|------------:|------------------:|
|       2 |          2 | VisMot       |           2 |                 8 |
|       4 |          2 | VisStat      |          -4 |               -64 |


## Threshold with threshold specified

### input

|   onset |   duration | trial_type   |   to_threshold |
|--------:|-----------:|:-------------|---------------:|
|       2 |          2 | VisMot       |              1 |
|       4 |          2 | VisStat      |              2 |
|       6 |          2 | VisMot       |             -1 |
|       8 |          2 | VisStat      |             -2 |

### transformation 

```json
{
    "Description": "Thresholdwiththresholdspecified",
    "Instruction": {
        "Name": "Threshold",
        "Input": "to_threshold",
        "Threshold": 1
    }
}
```

### output 

|   onset |   duration | trial_type   |   to_threshold |
|--------:|-----------:|:-------------|---------------:|
|       2 |          2 | VisMot       |              0 |
|       4 |          2 | VisStat      |              2 |
|       6 |          2 | VisMot       |              0 |
|       8 |          2 | VisStat      |              0 |


## Subtract

### input

|   onset |   duration | trial_type   |   intensity |
|--------:|-----------:|:-------------|------------:|
|       2 |          2 | VisMot       |           2 |
|       4 |          2 | VisStat      |          -4 |

### transformation 

```json
{
    "Description": "Subtract",
    "Instruction": {
        "Name": "Subtract",
        "Input": "onset",
        "Value": 3
    }
}
```

### output 

|   onset |   duration | trial_type   |   intensity |
|--------:|-----------:|:-------------|------------:|
|      -1 |          2 | VisMot       |           2 |
|       1 |          2 | VisStat      |          -4 |


## Product

### input

|   onset |   duration | trial_type   |   to_threshold |
|--------:|-----------:|:-------------|---------------:|
|       2 |          2 | VisMot       |              1 |
|       4 |          2 | VisStat      |              2 |
|       6 |          2 | VisMot       |             -1 |
|       8 |          2 | VisStat      |             -2 |

### transformation 

```json
{
    "Description": "Product",
    "Instruction": {
        "Name": "Product",
        "Input": [
            "onset",
            "duration"
        ],
        "Output": "onset_times_duration"
    }
}
```

### output 

|   onset |   duration | trial_type   |   to_threshold |   onset_times_duration |
|--------:|-----------:|:-------------|---------------:|-----------------------:|
|       2 |          2 | VisMot       |              1 |                      4 |
|       4 |          2 | VisStat      |              2 |                      8 |
|       6 |          2 | VisMot       |             -1 |                     12 |
|       8 |          2 | VisStat      |             -2 |                     16 |


## Threshold with output

### input

|   onset |   duration | trial_type   |   to_threshold |
|--------:|-----------:|:-------------|---------------:|
|       2 |          2 | VisMot       |              1 |
|       4 |          2 | VisStat      |              2 |
|       6 |          2 | VisMot       |             -1 |
|       8 |          2 | VisStat      |             -2 |

### transformation 

```json
{
    "Description": "Thresholdwithoutput",
    "Instruction": {
        "Name": "Threshold",
        "Input": "to_threshold",
        "Output": "tmp"
    }
}
```

### output 

|   onset |   duration | trial_type   |   to_threshold |   tmp |
|--------:|-----------:|:-------------|---------------:|------:|
|       2 |          2 | VisMot       |              1 |     1 |
|       4 |          2 | VisStat      |              2 |     2 |
|       6 |          2 | VisMot       |             -1 |     0 |
|       8 |          2 | VisStat      |             -2 |     0 |


## Divide several inputs

### input

|   onset |   duration | trial_type   |   intensity |
|--------:|-----------:|:-------------|------------:|
|       2 |          2 | VisMot       |           2 |
|       4 |          2 | VisStat      |          -4 |

### transformation 

```json
{
    "Description": "Divideseveralinputs",
    "Instruction": {
        "Name": "Divide",
        "Input": [
            "onset",
            "duration"
        ],
        "Value": 2
    }
}
```

### output 

|   onset |   duration | trial_type   |   intensity |
|--------:|-----------:|:-------------|------------:|
|       1 |          1 | VisMot       |           2 |
|       2 |          1 | VisStat      |          -4 |


## Threshold binarize above

### input

|   onset |   duration | trial_type   |   to_threshold |
|--------:|-----------:|:-------------|---------------:|
|       2 |          2 | VisMot       |              1 |
|       4 |          2 | VisStat      |              2 |
|       6 |          2 | VisMot       |             -1 |
|       8 |          2 | VisStat      |             -2 |

### transformation 

```json
{
    "Description": "Thresholdbinarizeabove",
    "Instruction": {
        "Name": "Threshold",
        "Input": "to_threshold",
        "Binarize": true,
        "Above": false
    }
}
```

### output 

|   onset |   duration | trial_type   |   to_threshold |
|--------:|-----------:|:-------------|---------------:|
|       2 |          2 | VisMot       |              0 |
|       4 |          2 | VisStat      |              0 |
|       6 |          2 | VisMot       |              1 |
|       8 |          2 | VisStat      |              1 |


## Subtract to specific rows

### input

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|
|       2 |          2 |            1 | Famous face     | Face         |            1.5  |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |
|       5 |          2 |            2 | Famous face     | Face         |            1.56 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |

### transformation 

```json
{
    "Description": "Subtracttospecificrows",
    "Instruction": {
        "Name": "Subtract",
        "Input": "onset",
        "Query": "response_time < 2",
        "Value": 1
    }
}
```

### output 

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|
|       1 |          2 |            1 | Famous face     | Face         |            1.5  |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |
|       4 |          2 |            2 | Famous face     | Face         |            1.56 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |


## Threshold binarize

### input

|   onset |   duration | trial_type   |   to_threshold |
|--------:|-----------:|:-------------|---------------:|
|       2 |          2 | VisMot       |              1 |
|       4 |          2 | VisStat      |              2 |
|       6 |          2 | VisMot       |             -1 |
|       8 |          2 | VisStat      |             -2 |

### transformation 

```json
{
    "Description": "Thresholdbinarize",
    "Instruction": {
        "Name": "Threshold",
        "Input": "to_threshold",
        "Binarize": true
    }
}
```

### output 

|   onset |   duration | trial_type   |   to_threshold |
|--------:|-----------:|:-------------|---------------:|
|       2 |          2 | VisMot       |              1 |
|       4 |          2 | VisStat      |              1 |
|       6 |          2 | VisMot       |              0 |
|       8 |          2 | VisStat      |              0 |


## Threshold

### input

|   onset |   duration | trial_type   |   to_threshold |
|--------:|-----------:|:-------------|---------------:|
|       2 |          2 | VisMot       |              1 |
|       4 |          2 | VisStat      |              2 |
|       6 |          2 | VisMot       |             -1 |
|       8 |          2 | VisStat      |             -2 |

### transformation 

```json
{
    "Description": "Threshold",
    "Instruction": {
        "Name": "Threshold",
        "Input": "to_threshold"
    }
}
```

### output 

|   onset |   duration | trial_type   |   to_threshold |
|--------:|-----------:|:-------------|---------------:|
|       2 |          2 | VisMot       |              1 |
|       4 |          2 | VisStat      |              2 |
|       6 |          2 | VisMot       |              0 |
|       8 |          2 | VisStat      |              0 |


## Sum with weights

### input

|   onset |   duration | trial_type   |   to_threshold |
|--------:|-----------:|:-------------|---------------:|
|       2 |          2 | VisMot       |              1 |
|       4 |          2 | VisStat      |              2 |
|       6 |          2 | VisMot       |             -1 |
|       8 |          2 | VisStat      |             -2 |

### transformation 

```json
{
    "Description": "Sumwithweights",
    "Instruction": {
        "Name": "Sum",
        "Input": [
            "onset",
            "duration"
        ],
        "Weights": [
            2,
            1
        ],
        "Output": "onset_plus_duration_with_weight"
    }
}
```

### output 

|   onset |   duration | trial_type   |   to_threshold |   onset_plus_duration_with_weight |
|--------:|-----------:|:-------------|---------------:|----------------------------------:|
|       2 |          2 | VisMot       |              1 |                                 6 |
|       4 |          2 | VisStat      |              2 |                                10 |
|       6 |          2 | VisMot       |             -1 |                                14 |
|       8 |          2 | VisStat      |             -2 |                                18 |
