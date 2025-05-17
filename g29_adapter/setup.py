from setuptools import find_packages, setup

package_name = 'g29_adapter'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='halir',
    maintainer_email='halirszabi@gmail.com',
    description='This is an adapter for the Logitech G29 steering wheel, which converts joystick inputs to throttle and steering commands.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'adapter = g29_adapter.adapter:main'
        ],
    },
)
