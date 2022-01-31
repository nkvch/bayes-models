## Modele Bayesowskie
*Stanislau Stankevich*

W ramach ćwiczenie zdefiniowano następujący problem:

![](./graf.png)

Gdzie prawdopodobieństwa:

|       | Budzik był ustawiony |
|-------|----------------------|
| True  | 0.85                 |
| False | 0.15                 |

|       | Telefon był podłączony do ładowarki |
|-------|-------------------------------------|
| True  | 0.7                                 |
| False | 0.3                                 |

| Telefon był podłączony do ładowarki | Telefon się wyłączył (p-stwo) |
|-------------------------------------|-------------------------------|
| True                                | 0.02                          |
| False                               | 0.77                          |

| Budzik był ustawiony | Telefon się wyłączył (p-stwo) | Budzik zadzwonił |
|----------------------|-------------------------------|------------------|
| False                | False                         | 0.001            |
| False                | True                          | 0                |
| True                 | False                         | 0.99             |
| True                 | True                          | 0                |

| Budzik zadzownił | Zaspanie |
|------------------|----------|
| True             | 0.05     |
| False            | 0.86     |