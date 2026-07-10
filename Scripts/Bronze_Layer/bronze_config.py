BASEPATH = "/Volumes/workspace/bronze/source_systems"

INGESTION_CONFIG = [
    # CRM
    {
        "source": "crm",
        "path": f"{BASEPATH}/source_crm/cust_info.csv",
        "table": "crm_cust_info"
    },
    {
        "source": "crm",
        "path": f"{BASEPATH}/source_crm/prd_info.csv",
        "table": "crm_prd_info"
    },
    {
        "source": "crm",
        "path": f"{BASEPATH}/source_crm/sales_details.csv",
        "table": "crm_sales_details"
    },

    # ERP
    {
        "source": "erp",
        "path": f"{BASEPATH}/source_erp/CUST_AZ12.csv",
        "table": "erp_cust_az12"
    },
    {
        "source": "erp",
        "path": f"{BASEPATH}/source_erp/LOC_A101.csv",
        "table": "erp_loc_a101"
    },
    {
        "source": "erp",
        "path": f"{BASEPATH}/source_erp/PX_CAT_G1V2.csv",
        "table": "erp_px_cat_g1v2"
    }
]
