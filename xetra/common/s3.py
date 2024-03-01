"""
Connector and methods accessing S3
"""

import os

import logging as log

import boto3


class S3BucketConnector():
    """
    Class for interacting with S3 buckets
    """

#used to initialize an object and create an instance of it.
#using the "self" keyword informs that we're using an instance method
    def __init__(self, access_key: str, secret_key: str, endpoint_url: str, bucket: str):
        """
        Constructor for S3BucketConnector

        :param access_key: access key for accessing S3
        :param secret_key: secret key for accessing S3
        :param endpopint_url: endpoint url for S3
        :param bucket: S3 bucket name
        """
        self._logger = log.getLogger(__name__)
        self.endpoint_url = endpoint_url
        self.session = boto3.Session(aws_access_key_id = os.environ[access_key],
                                     aws_secret_access_key = os.environ[secret_key])
        self._s3 = self.session.resource(service_name='s3',endpoint_url=endpoint_url)
        self._bucket = self._s3.Bucket(bucket)


    def list_files_in_prefix(self, prefix: str):
        """
        listing all files with a prefix on the S3 bucket

        :param prefix: prefix on the S3 buckets that should be filtered with

        returns: 
            files: list of all filenames containing the prefix in the key
        """
        files = [obj.key for obj in self._bucket.objects.filter(Prefix=prefix)]
        return files

    def read_csv_to_df(self):
        pass

    def write_df_to_s3(self):
        pass
