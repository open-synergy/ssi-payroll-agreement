import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-payroll-agreement",
    description="Meta package for open-synergy-ssi-payroll-agreement Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_payroll_agreement',
        'odoo14-addon-ssi_payroll_agreement_documenso_signing',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
