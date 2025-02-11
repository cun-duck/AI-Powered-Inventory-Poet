import argparse
from data_cleaner.excel_processor import InventoryCleaner
from data_cleaner.data_validator import DataValidator
from narrative_generator.gpt_integration import ReportWriter
from report_builder.dashboard import create_dashboard
import os

def main(input_file):
    # Data Processing
    cleaner = InventoryCleaner(input_file)
    df = cleaner.clean_data()
    
    DataValidator.validate_structure(df)
    DataValidator.validate_data_types(df)
    
    # Report Generation
    writer = ReportWriter()
    narrative = writer.generate_report(df)
    
    # Dashboard Creation
    dashboard_html = create_dashboard(df, narrative)
    
    # Save Output
    with open("inventory_report.html", "w") as f:
        f.write(dashboard_html)
        
    print("Report generated successfully: inventory_report.html")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    
    main(args.input)
