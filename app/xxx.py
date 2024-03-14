from schemas import DeviceWholeSchema


input = '''
<DeviceWholeSchema>
	<name>string</name>
	<type>string</type>
	<ip_address>string</ip_address>
	<subnet_mask>string</subnet_mask>
	<gateway>string</gateway>
	<dns_servers>
		<dns_server>stri1</dns_server>
        <dns_server>strin2</dns_server>
        <dns_server>strin3</dns_server>
	</dns_servers>
	<interfaces>
		<interface>
			<name>strin2g</name>
			<ip_address>string</ip_address>
			<subnet_mask>string</subnet_mask>
			<status>string</status>
		</interface>
		<interface>
			<name>strin2g123</name>
			<ip_address>string</ip_address>
			<subnet_mask>string</subnet_mask>
			<status>string</status>
		</interface>
		<interface>
			<name>strin2g123123</name>
			<ip_address>string</ip_address>
			<subnet_mask>string</subnet_mask>
			<status>string</status>
		</interface>
	</interfaces>
	<routing_table>
		<routes>
			<destination>stri3ng</destination>
			<gateway>string</gateway>
			<interface_name>string</interface_name>
		</routes>

		<routes>
			<destination>stri3ng</destination>
			<gateway>string</gateway>
			<interface_name>string</interface_name>
		</routes>

		<routes>
			<destination>stri3ng</destination>
			<gateway>string</gateway>
			<interface_name>string</interface_name>
		</routes>
	</routing_table>
</DeviceWholeSchema>
'''

x = DeviceWholeSchema.from_xml(input)

print(x)