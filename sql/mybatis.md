# 教程
## for循环
```xml
<if test="neIds.size()!=0">
	and NE_ID IN
	<foreach collection="neIds" item="neId" index="index" open="(" separator="," close=")">
		#{neId}
	</foreach>
</if>
```