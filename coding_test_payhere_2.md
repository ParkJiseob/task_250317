### 과제2. 아래의 요구사항에 맞는 데이터 파이프라인 아키텍처를 제시하시오. 
#### 요구사항 
    - 상점의 30분전까지의 집계 데이터를 보여줘야 한다.
        - 집계 데이터 종류 : 결제 금액 합산, 상품 수
    - 단, 실 서비스에 영향이 없어야 한다.
    - AWS 혹은 GCP 클라우드 환경을 고려할 것

1. AWS DMS를 활용한 방법
![Image](https://github.com/user-attachments/assets/c6a9253e-de9f-41bc-8fa1-6454fa1a3b82)
    - AWS DMS는 RDS의 binlog 또는 MongoDB의 oplog를 통해 상용 데이터의 실시간 이행이 가능하다.
    - 규모가 클 경우 S3 등에 임시 저장하는 방법도 고려할 수 있다. 
    - MongoDB의 경우 NoSQL이므로, S3에 임시 저장 후 Glue 또는 Lambda를 활용하여 관계형으로 변환한다.
    - DMS의 target endpoint로 Redshift Serverless를 활용한다. (GCP의 경우 BigQuery도 가능)
    - 최종적으로 QuickSight 또는 기존에 사용중인 BI Tool과 연동하여 준실시간으로 집계 데이터를 확인할 수 있다.


2. AWS Kinesis를 활용한 방법   
![Image](https://github.com/user-attachments/assets/bd791487-4ed2-4044-bcd8-654bfd304d9c)
    - Kinesis Data Streams를 활용하여 순차적으로 실시간 이행이 가능하다.
    - Firehose를 사용하면 데이터 변환, 압축, 적재를 지원하므로 수동으로 처리할 필요가 줄어든다.
    - 중간에 Lambda를 활용하여 데이터 변환, 필터링, 집계 등의 작업이 가능하다. (Kinesis Data Analytics도 가능)
    - 이후 Redshift Serverless와 같은 DW에 데이터를 담는다.
    - 최종적으로 QuickSight 또는 기존에 사용중인 BI Tool과 연동하여 준실시간으로 집계 데이터를 확인할 수 있다.