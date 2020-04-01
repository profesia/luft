# -*- coding: utf-8 -*-
"""BigQuery Load Task Schema."""
from luft.schemas.bq_load_task_schema import BQLoadTaskSchema
from luft.tasks.bq_load_staging_task import BQLoadStagingTask

from marshmallow import fields, post_load


class BQLoadStagingTaskSchema(BQLoadTaskSchema):
    """BigQuery Load Task Schema."""

    @post_load
    def make_task(self, data, **kwargs):

        return BQLoadStagingTask(**kwargs)
