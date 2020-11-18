

import re;

pojo = '''
	/**
	 * 主键标识ID.
	 */
	@Id
	@Column(name = "ID")
	private Long id;

	@Column(name = "DATASOURCE_NAME")
	private String datasourceName;

	@Column(name = "DATASOURCE_ID")
	private Long datasourceId;

	/**
	 * 账号ID.
	 */
	@Column(name = "ACCOUNT_ID")
	private Long accountId;

	@Column(name = "ACCOUNT_NAME")
	private String accountName;

	/**
	 * 专业ID.
	 */
	@Column(name = "SPECIALTY_ID")
	private Long specialtyId;

	/**
	 * 专业名称
	 */
	@Column(name = "SPECIALTY_NAME")
	private String specialtyName;

	/**
	 * 设备类型ID.
	 */
	@Column(name = "DEVICE_TYPE_ID")
	private Long deviceTypeId;

	/**
	 * 设备类型名称.
	 */
	@Column(name = "DEVICE_TYPE_NAME")
	private String deviceTypeName;

	/**
	 * 设备类型ID.
	 */
	@Column(name = "VENDOR_ID")
	private Long vendorId;

	/**
	 * 设备类型名称.
	 */
	@Column(name = "VENDOR_NAME")
	private String vendorName;


	/**
	 * 修改时间
	 */
	@Column(name = "CREATE_TIME")
	private Date createTime;
	/**
	 * 新建时间
	 */
	@Column(name = "UPDATE_TIME")
	private Date updateTime;

'''

if __name__ == '__main__':
    for column,var in re.findall("(?s)@Column.*?\"(\w+?)\".*?private.*?\s+(\w+);",pojo):
        print(f"<result column=\"{column}\" property=\"{var}\"/>")
