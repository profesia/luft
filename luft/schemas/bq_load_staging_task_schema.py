# -*- coding: utf-8 -*-
"""BigQuery Load Task Schema."""
from luft.schemas.bq_load_task_schema import BQLoadTaskSchema
from luft.tasks.bq_load_staging_task import BQLoadStagingTask

from marshmallow import fields, post_load


class BQLoadStagingTaskSchema(BQLoadTaskSchema):
    """BigQuery Load Task Schema."""

    @post_load
    def make_task(self, data, **kwargs):

        return BQLoadStagingTask(name=data.get('name'), task_type=data.get('task_type'),
                          source_system=data.get('source_system'),
                          source_subsystem=data.get('source_subsystem'),
                          columns=data.get('columns'),
                          project_id=data.get('project_id'),
                          location=data.get('location'),
                          dataset_id=data.get('dataset_id'),
                          skip_leading_rows=data.get('skip_leading_rows'),
                          disable_check=data.get('disable_check'),
                          field_delimiter=data.get('field_delimiter'),
                          path_prefix=data.get('path_prefix'),
                          yaml_file=data.get('yaml_file'), env=data.get('env'),
                          thread_name=data.get('thread_name'), color=data.get('color'))
