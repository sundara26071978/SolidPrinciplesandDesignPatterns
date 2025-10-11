import json
from datetime import datetime
from typing import Protocol,Any
import pandas as pd

class SalesReader(Protocol):
    def read(self, input_file: str) -> pd.DataFrame:
        ...

class CSVSalesReader:
    def read(self, input_file: str) -> pd.DataFrame:
        return pd.read_csv(input_file, parse_dates=["date"])
    
class ReportWriter(Protocol):
    def write(self, output_file: str, report: dict[str, Any]) -> None:
        ...

class JSONReportWriter:
    def write(self, output_file: str, report: dict[str, Any]) -> None:
        with open(output_file, "w") as f:
            json.dump(report, f, indent=2)
class DataRangeFilter:
    def __init__(self, start_date: datetime | None = None, end_date: datetime | None = None):
        self.start_date = start_date
        self.end_date = end_date
    def filter(self, df: pd.DataFrame) -> pd.DataFrame:
        if self.start_date:
            df = df[df["date"] >= self.start_date]
        if self.end_date:
            df = df[df["date"] <= self.end_date]
        return df   
    
class Metric(Protocol):
    def compute(self, df: pd.DataFrame) -> dict[str, Any]:
        ...
class CustomerCountMetric:
    def compute(self, df):
        return {"number_of_customers": df["name"].nunique()}
class AverageOrderValueMetric:
    def compute(self, df)->dict[str,Any]:
        avg_order = (
            df[df["price"] > 0]["price"].mean() if not df[df["price"] > 0].empty else 0
        )
        return {"average_order_value (pre-tax)": round(avg_order, 2)}
class ReturnPercentageMetric:
    def compute(self, df)->dict[str,Any]:
        returns = df[df["price"] < 0]
        return_pct = (len(returns) / len(df)) * 100 if len(df) > 0 else 0
        return {"return_percentage": round(return_pct, 2)}
class TotalSalesMetric:
    def compute(self, df)->dict[str,Any]:
        return {"total_sales": round(df["price"].sum(), 2)}
    
        
class SalesReportGenerator:

    def __init__(self, reader:SalesReader,writer: ReportWriter,metrics: list[Metric]) -> None:
        self.reader=reader
        self.writer=writer
        self.metrics = metrics

    def generate(
        self,
        input_file: str,
        output_file: str,
        filter :DataRangeFilter | None = None,
    ) -> None:
       
        df=self.reader.read(input_file)
        
        if filter:
            df = filter.filter(df)

       
        report_data = {}
        for metric in self.metrics:
            report_data.update(metric.compute(df))
       
        report = {
            "report_start": filter.start_date.strftime("%Y-%m-%d") if filter.start_date else "N/A",
            "report_end": filter.end_date.strftime("%Y-%m-%d") if filter.end_date else "N/A",
            **report_data,
        }

        self.writer.write(output_file, report)


def main() -> None:
    SalesReader = CSVSalesReader()
    writer = JSONReportWriter()

    report = SalesReportGenerator(
        reader=SalesReader,
        writer=writer,
        metrics = [CustomerCountMetric(), 
                    AverageOrderValueMetric(), 
                    ReturnPercentageMetric(), 
                    TotalSalesMetric()]
        )
    
    report.generate(
        input_file="sales_data.csv",
        output_file="sales_report.json",
        filter =DataRangeFilter(start_date=datetime(2024, 7, 1),
        end_date=datetime(2024, 12, 31))
    )


if __name__ == "__main__":
    main()
