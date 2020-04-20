import setuptools

setuptools.setup(
	name = "aplicativo",
	packages = setuptools.find_packages(),

	entry_points = {
		"console_scripts": [
			"aplicativo = src.aplicativo.__init__:main"
		]
	}
)
