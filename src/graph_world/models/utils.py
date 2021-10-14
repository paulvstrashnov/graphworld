# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import random

import numpy as np
from sklearn.metrics import mean_squared_error

def MseWrapper(pred, true, scale=False):
  """Wrapper for Mean-Squared-Error eval metric.

  Arguments:
    pred: iterable of predicted values
    true: iterable of true values
    scale: if True, return value is divided by var(true)
  """
  mse = mean_squared_error(pred, true)
  if scale:
    mse /= np.var(true)
  return mse


def ComputeNumPossibleConfigs(benchmark_params, h_params):
  num_possible_configs = 1
  if benchmark_params is not None:
    for _, value_list_or_value in benchmark_params.items():
      try:
        num_possible_configs *= len(value_list_or_value)
      except TypeError:
        continue
  if h_params is not None:
    for _, value_list_or_value in h_params.items():
      try:
        num_possible_configs *= len(value_list_or_value)
      except TypeError:
        continue
  return num_possible_configs


def _SampleValue(value_list_or_value):
  try:
    value = random.choice(value_list_or_value)
  except TypeError:
    value = value_list_or_value
  return value


def SampleModelConfig(benchmark_params, h_params):
  """Samples a model config from dictionaries of hyperparameter lists.

  """
  if benchmark_params is None:
    benchmark_params_sample = None
  else:
    benchmark_params_sample = {
      name: _SampleValue(value_list_or_value) for
      name, value_list_or_value in benchmark_params.items()
    }
  if h_params is None:
    h_params_sample = None
  else:
    h_params_sample = {
      name: _SampleValue(value_list_or_value) for
      name, value_list_or_value in h_params.items()
    }
  return benchmark_params_sample, h_params_sample
