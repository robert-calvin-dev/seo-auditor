import argparse
from seo_auditor.auditor import SEOAuditor

def main():
    parser = argparse.ArgumentParser(
        description="SEO Site Auditor - Crawl a website and generate SEO reports in CSV and HTML format."
    )
    parser.add_argument(
        "url",
        type=str,
        help="The base URL of the website to audit (include http/https)."
    )
    parser.add_argument(
        "--email",
        action="store_true",
        help="Send the report via email if smtp.json is configured."
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="reports",
        help="Directory to save reports (default: ./reports)"
    )
    parser.add_argument(
        "--template-dir",
        type=str,
        default="seo_auditor/templates",
        help="Directory where the HTML templates are stored (default: seo_auditor/templates)"
    )
    parser.add_argument(
        "--config-dir",
        type=str,
        default="seo_auditor/config",
        help="Directory for smtp.json config (default: seo_auditor/config)"
    )

    args = parser.parse_args()

    auditor = SEOAuditor(
        base_url=args.url,
        output_dir=args.output_dir,
        template_dir=args.template_dir,
        config_dir=args.config_dir
    )
    print(f"[*] Starting crawl for {args.url}...")
    auditor.crawl()

    print("[*] Generating reports...")
    csv_report, html_report = auditor.save_report()
    print(f"[+] CSV report saved to {csv_report}")
    print(f"[+] HTML report saved to {html_report}")

    if args.email:
        print("[*] Sending report via email...")
        auditor.send_email_report(html_report)

if __name__ == "__main__":
    main()
