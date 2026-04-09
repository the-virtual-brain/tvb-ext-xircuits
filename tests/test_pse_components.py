# -*- coding: utf-8 -*-
#
# Unit tests for PSE components
#
import pytest
import numpy

from xai_components.base import InArg, OutArg


def _set(comp, attr, val):
    setattr(comp, attr, InArg(val))


def _out(comp, attr):
    setattr(comp, attr, OutArg(None))


class TestPSELinspaceRange:

    def _make(self, start=0.0, stop=1.0, num_points=5):
        from xai_components.xai_pse.range_components import PSELinspaceRange
        comp = PSELinspaceRange()
        _set(comp, 'start', start)
        _set(comp, 'stop', stop)
        _set(comp, 'num_points', num_points)
        _out(comp, 'values')
        return comp

    def test_basic_range(self):
        comp = self._make(0.0, 1.0, 5)
        comp.execute({})
        result = comp.values.value
        assert len(result) == 5
        numpy.testing.assert_allclose(result, [0.0, 0.25, 0.5, 0.75, 1.0])

    def test_two_points(self):
        comp = self._make(0.0, 10.0, 2)
        comp.execute({})
        assert comp.values.value == [0.0, 10.0]

    def test_output_is_list(self):
        comp = self._make(0.0, 1.0, 3)
        comp.execute({})
        assert isinstance(comp.values.value, list)

    def test_large_range(self):
        comp = self._make(0.0, 100.0, 101)
        comp.execute({})
        assert len(comp.values.value) == 101

    def test_invalid_num_points_zero(self):
        comp = self._make(0.0, 1.0, 0)
        with pytest.raises(ValueError, match="num_points must be >= 1"):
            comp.execute({})

    def test_start_ge_stop(self):
        comp = self._make(5.0, 2.0, 10)
        with pytest.raises(ValueError, match="start.*must be < stop"):
            comp.execute({})

    def test_defaults_when_none(self):
        from xai_components.xai_pse.range_components import PSELinspaceRange
        comp = PSELinspaceRange()
        _set(comp, 'start', None)
        _set(comp, 'stop', None)
        _set(comp, 'num_points', None)
        _out(comp, 'values')
        comp.execute({})
        assert len(comp.values.value) == 10
        assert comp.values.value[0] == 0.0
        assert comp.values.value[-1] == 1.0


class TestPSEArangeRange:

    def _make(self, start=0.0, stop=1.0, step=0.25):
        from xai_components.xai_pse.range_components import PSEArangeRange
        comp = PSEArangeRange()
        _set(comp, 'start', start)
        _set(comp, 'stop', stop)
        _set(comp, 'step', step)
        _out(comp, 'values')
        return comp

    def test_basic_arange(self):
        comp = self._make(0.0, 1.0, 0.25)
        comp.execute({})
        result = comp.values.value
        assert len(result) == 4
        numpy.testing.assert_allclose(result, [0.0, 0.25, 0.5, 0.75])

    def test_output_is_list(self):
        comp = self._make(0.0, 0.5, 0.1)
        comp.execute({})
        assert isinstance(comp.values.value, list)

    def test_negative_step_raises(self):
        comp = self._make(0.0, 1.0, -0.1)
        with pytest.raises(ValueError, match="step must be > 0"):
            comp.execute({})

    def test_start_ge_stop_raises(self):
        comp = self._make(5.0, 2.0, 0.1)
        with pytest.raises(ValueError, match="start.*must be < stop"):
            comp.execute({})


class TestPSEValueList:

    def _make(self, csv_string):
        from xai_components.xai_pse.range_components import PSEValueList
        comp = PSEValueList()
        _set(comp, 'values_string', csv_string)
        _out(comp, 'values')
        return comp

    def test_parse_csv(self):
        comp = self._make("0.1, 0.5, 1.0, 2.5")
        comp.execute({})
        assert comp.values.value == [0.1, 0.5, 1.0, 2.5]

    def test_single_value(self):
        comp = self._make("42.0")
        comp.execute({})
        assert comp.values.value == [42.0]

    def test_whitespace(self):
        comp = self._make("  1.0 ,  2.0 ,  3.0  ")
        comp.execute({})
        assert comp.values.value == [1.0, 2.0, 3.0]

    def test_empty_raises(self):
        comp = self._make("")
        with pytest.raises(ValueError, match="cannot be empty"):
            comp.execute({})

    def test_none_raises(self):
        comp = self._make(None)
        with pytest.raises(ValueError, match="cannot be empty"):
            comp.execute({})

    def test_non_numeric_raises(self):
        comp = self._make("a, b, c")
        with pytest.raises(ValueError, match="could not parse"):
            comp.execute({})


class TestPSEParameterGrid:

    def _make(self, p1, p2, name1="coupling", name2="speed"):
        from xai_components.xai_pse.grid_components import PSEParameterGrid
        comp = PSEParameterGrid()
        _set(comp, 'param1_values', p1)
        _set(comp, 'param2_values', p2)
        _set(comp, 'param1_name', name1)
        _set(comp, 'param2_name', name2)
        _out(comp, 'grid_combinations')
        _out(comp, 'param1_axis')
        _out(comp, 'param2_axis')
        _out(comp, 'grid_shape')
        _out(comp, 'total_simulations')
        return comp

    def test_basic_grid(self):
        comp = self._make([1.0, 2.0, 3.0], [10.0, 20.0])
        comp.execute({})
        combos = comp.grid_combinations.value
        assert len(combos) == 6
        assert (1.0, 10.0) in combos
        assert (3.0, 20.0) in combos

    def test_grid_shape(self):
        comp = self._make([1.0, 2.0], [5.0, 6.0, 7.0])
        comp.execute({})
        assert comp.grid_shape.value == (2, 3)
        assert comp.total_simulations.value == 6

    def test_single_values(self):
        comp = self._make([1.0], [2.0])
        comp.execute({})
        assert comp.grid_combinations.value == [(1.0, 2.0)]
        assert comp.total_simulations.value == 1

    def test_context_metadata(self):
        ctx = {}
        comp = self._make([1.0, 2.0], [5.0], "G", "tau")
        comp.execute(ctx)
        assert ctx["pse_param1_name"] == "G"
        assert ctx["pse_param2_name"] == "tau"
        assert ctx["pse_grid_shape"] == (2, 1)

    def test_empty_param1_raises(self):
        comp = self._make([], [1.0])
        with pytest.raises(ValueError, match="param1_values is empty"):
            comp.execute({})

    def test_none_param2_raises(self):
        comp = self._make([1.0], None)
        with pytest.raises(ValueError, match="param2_values is empty"):
            comp.execute({})


class TestPSEResultCollector:

    def _make(self, single, accumulated):
        from xai_components.xai_pse.metric_components import PSEResultCollector
        comp = PSEResultCollector()
        _set(comp, 'single_result', single)
        _set(comp, 'accumulated', accumulated)
        _out(comp, 'accumulated_out')
        _out(comp, 'count')
        return comp

    def test_first_collection(self):
        comp = self._make(numpy.array([1, 2, 3]), None)
        comp.execute({})
        assert comp.count.value == 1
        assert len(comp.accumulated_out.value) == 1

    def test_accumulation(self):
        existing = [numpy.array([1, 2]), numpy.array([3, 4])]
        comp = self._make(numpy.array([5, 6]), existing)
        comp.execute({})
        assert comp.count.value == 3

    def test_none_result_raises(self):
        comp = self._make(None, [])
        with pytest.raises(ValueError, match="single_result is None"):
            comp.execute({})


class TestPSEGlobalVariance:

    def _make(self, results, shape):
        from xai_components.xai_pse.metric_components import PSEGlobalVariance
        comp = PSEGlobalVariance()
        _set(comp, 'simulation_results', results)
        _set(comp, 'grid_shape', shape)
        _out(comp, 'metric_values')
        _out(comp, 'metric_matrix')
        _out(comp, 'metric_name')
        return comp

    def test_zero_variance(self):
        results = [numpy.zeros(100), numpy.ones(100)]
        comp = self._make(results, (1, 2))
        comp.execute({})
        assert comp.metric_values.value[0] == 0.0
        assert comp.metric_values.value[1] == 0.0

    def test_nonzero_variance(self):
        results = [numpy.arange(100, dtype=float)]
        comp = self._make(results, (1, 1))
        comp.execute({})
        assert comp.metric_values.value[0] > 0

    def test_matrix_shape(self):
        results = [numpy.random.randn(50) for _ in range(6)]
        comp = self._make(results, (2, 3))
        comp.execute({})
        assert comp.metric_matrix.value.shape == (2, 3)

    def test_metric_name(self):
        results = [numpy.array([1.0])]
        comp = self._make(results, (1, 1))
        comp.execute({})
        assert comp.metric_name.value == "Global Variance"

    def test_empty_raises(self):
        comp = self._make([], (0, 0))
        with pytest.raises(ValueError, match="no simulation results"):
            comp.execute({})


class TestPSEVarianceOfVariance:

    def _make(self, results, shape):
        from xai_components.xai_pse.metric_components import PSEVarianceOfVariance
        comp = PSEVarianceOfVariance()
        _set(comp, 'simulation_results', results)
        _set(comp, 'grid_shape', shape)
        _out(comp, 'metric_values')
        _out(comp, 'metric_matrix')
        _out(comp, 'metric_name')
        return comp

    def test_uniform_low_vov(self):
        uniform = numpy.ones((100, 1, 10, 1))
        comp = self._make([uniform], (1, 1))
        comp.execute({})
        assert comp.metric_values.value[0] == 0.0

    def test_heterogeneous_high_vov(self):
        ts = numpy.zeros((100, 1, 5, 1))
        for region in range(5):
            ts[:, 0, region, 0] = numpy.random.randn(100) * (region + 1)
        comp = self._make([ts], (1, 1))
        comp.execute({})
        assert comp.metric_values.value[0] > 0

    def test_metric_name(self):
        results = [numpy.random.randn(50, 1, 10, 1)]
        comp = self._make(results, (1, 1))
        comp.execute({})
        assert comp.metric_name.value == "Variance of Variance"

    def test_empty_raises(self):
        comp = self._make([], None)
        with pytest.raises(ValueError, match="no simulation results"):
            comp.execute({})
