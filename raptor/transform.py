import pandas as pd


class TransformMixin(object):
    def transform(self, df):
        return df


class TrasformPipeline(object):
    def __init__(self, stages):
        self.stages = []
        for stage in stages:
            if isinstance(stage, TransformMixin):
                self.stages.append(stage)

    def transform(self, df):
        df_copy = df.copy()
        for stage in self.stages:
            df_copy = stage.transform(df_copy)
        return df_copy


class GroupBy(TransformMixin):
    def __init__(self, **kwds):
        self.kwds = kwds

    def transform(self, df):
        return df.groupby(**self.kwds).sum()


class Pivot(TransformMixin):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def transform(self, df):
        return pd.pivot_table(df, **self.kwargs)
