{
    "name": "Drivers Info" ,
            "version": "1.3",
    "depends": [
        'base', 'account',
    ],
    "author": "Ayman/Yousif",
    "category": "Drivers",
    "website": "https://facebook.com/yousif-mobark",
    "support": "odoo@gvitt.com",
    "images": ["static/description/assets/main_screenshot.gif", "static/description/assets/main_screenshot.png",
               "static/description/assets/ghits_desktop_inv.jpg",
               "static/description/assets/ghits_labtop1.jpg"],
    "price": "0",
    "license": "OPL-1",
    "currency": "USD",
    "description": """
    this is a module to help you to save information about the drivers
    """
    ,
    "data": [
            "view/car.xml",'view/view.xml',"view/em.xml","view/trafficlines.xml","security/ir.model.access.csv"

    ],
    "installable": True,
    "auto_install": False,
    "application": True,
}
