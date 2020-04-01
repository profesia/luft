# -*- coding: utf-8 -*-
"""BigQuery Load Task."""
from pathlib import Path

from luft.common.config import ( BQ_STAGE_NO_HIST_DEFAULT_TEMPLATE )
from luft.common.logger import setup_logger
from luft.common.utils import NoneStr
from luft.tasks.bq_load_task import BQLoadTask

import pkg_resources

# Setup logger
logger = setup_logger('common', 'INFO')


class BQLoadStagingTask(BQLoadTask):
    """BQ Load without history task."""
    load_count = 0
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __call__(self, ts: str, env: NoneStr = None):
        """Make class callable.

        Attributes:
            ts (str): time of valid.

        """
        no_hist_stage_template = Path(pkg_resources.resource_filename('luft', BQ_STAGE_NO_HIST_DEFAULT_TEMPLATE))
        env_vars = self.get_env_vars(ts, env)

        if (BQLoadStagingTask.load_count is 0):
            self._create_dataset(self.stage_dataset_id)
            self._run_bq_command(no_hist_stage_template.parent, [no_hist_stage_template.name],
                                 env_vars)

        BQLoadStagingTask.load_count += 1
        self.load_csv()



