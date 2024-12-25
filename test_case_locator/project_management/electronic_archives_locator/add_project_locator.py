from selenium.webdriver.common.by import By


class AddProjectLocator():


    add_project_button_loc = (By.XPATH, '//*[text()="新增项目"]')

    # 保存
    save_button_loc = (By.XPATH, '//*[text()="保 存"]')
    # 上一步
    previous_button_loc = (By.XPATH, '//*[text()="上一步"]')
    # 下一步
    next_button_loc = (By.XPATH, '//*[text()="下一步"]')
    # 提交
    submit_button_loc = (By.XPATH, '//*[text()="提 交"]')
    # 关闭按钮
    close_button_loc = (By.XPATH, '//*[text()="关闭"]')
    """
    新增项目界面的元素
    由于元素太多了，每个页面再写一个类
    """
    # =====================项目基础资料维护=====================
    class ProjectBaseInfoLocator():
        # ===============项目基础资料维护======================
        # 立项时间选择框
        project_time_select_loc = (By.XPATH, '//*[@class="ant-select-selection-search"]')
        # 项目名称输入框
        project_name_input_loc = (By.XPATH, '//*[@placeholder="请输入项目名称"]')
        # 项目装机功率输入框
        project_install_power_input_loc = (By.XPATH, '//*[@placeholder="请输入装机功率"]')
        # 项目装机容量输入框
        project_install_capacity_input_loc = (By.XPATH, '//*[@placeholder="请输入装机容量"]')
        # 项目阶段选择框
        project_stage_select_loc = (By.XPATH, '//*[@class="ant-select-selection-search"]')
        # 项目阶段 - 待实施阶段
        project_stage_wait_for_implementation_loc = (By.XPATH, '//*[@title="待实施阶段"]')
        # 项目阶段 - 实施阶段
        project_stage_implementation_loc = (By.XPATH, '//*[@title="实施阶段"]')
        # 项目阶段 - 售后阶段
        project_stage_after_sale_loc = (By.XPATH, '//*[@title="售后阶段"]')
        # 项目进度选择框
        project_progress_select_loc = (By.XPATH, '//*[@class="ant-select-selection-search"]')
        # 项目进度 -计划期
        project_progress_plan_loc = (By.XPATH, '//*[@title="计划期"]')
        # 项目进度 -准备期
        project_progress_preparation_loc = (By.XPATH, '//*[@title="实施阶段（准备期）"]')
        # 项目进度 -发货期
        project_progress_send_out_goods_loc = (By.XPATH, '//*[@title="发货期"]')
        # 项目进度 -调试期
        project_progress_debug_loc = (By.XPATH, '//*[@title="调试期"]')
        # 项目进度 -试运行
        project_progress_test_run_loc = (By.XPATH, '//*[@title="试运行"]')
        # 项目进度 - 质保期
        project_progress_warranty_loc = (By.XPATH, '//*[@title="质保期"]')
        # 项目进度 - 已过保
        project_progress_warranty_expired_loc = (By.XPATH, '//*[@title="已过保"]')
        # 项目类型
        project_type_select_loc = (By.XPATH, '//*[@class="ant-select-selection-search"]')
        # 项目类型 -工商业
        project_type_commercial_loc = (By.XPATH, '//*[@title="商用"]')
        # 项目类型 - 电网侧
        project_type_electricity_side_loc = (By.XPATH, '//*[@title="电网侧"]')
        # 项目类型 - 电源侧
        project_type_power_side_loc = (By.XPATH, '//*[@title="电源侧"]')

        # 产品类型
        product_type_select_loc = (By.XPATH, '//*[@class="ant-select-selection-search"]')
        # 产品类型 - 非系统
        product_type_non_system_loc = (By.XPATH, '//*[@title="非系统"]')
        # 产品类型 - 集装箱
        product_type_container_loc = (By.XPATH, '//*[@title="集装箱"]')
        # 产品类型 - 外户柜
        product_type_outdoor_cabinet_loc = (By.XPATH, '//*[@title="户外柜"]')

        # 所属区域选择框
        work_order_area_select_loc = (By.XPATH, '//*[@class="ant-select-selection-search"]')
        # 所属区域 - 东部
        project_area_east_loc = (By.XPATH, '//*[@title="东部"]')
        # 所属区域 - 西北
        project_area_northwest_loc = (By.XPATH, '//*[@title="西北"]')
        # 所属区域 - 南方
        project_area_south_loc = (By.XPATH, '//*[@title="南方"]')
        # 所属区域 -  海外
        project_area_overseas_loc = (By.XPATH, '//*[@title="海外"]')
        # 所属区域 - 大储运维（宁夏）
        project_area_ningxia_loc = (By.XPATH, '//*[@title="大储运维（宁夏）"]')

        # 是否支持巡检标准
        # 是否支持巡检标准 - 是
        is_support_inspection_standard_yes_loc = (By.XPATH, '//*[@title="是"]')
        # 是否支持巡检标准 - 否
        is_support_inspection_standard_no_loc = (By.XPATH, '//*[@title="否"]')

        # 保存
        save_button_loc = (By.XPATH, '//*[text()="保 存"]')
        # 下一步
        next_button_loc = (By.XPATH, '//*[text()="下一步"]')


    # =====================项目详细资料维护=====================
    class ProjectDetailInfoLocator():
        # 电站详细信息
        # 业主名称输入框
        owner_name_input_loc = (By.XPATH, '//*[@placeholder="请输入业主名称"]')
        # 项目地址输入框
        project_address_input_loc = (By.XPATH, '//*[@placeholder="请输入项目地址"]')
        # 电站名称输入框
        station_name_input_loc = (By.XPATH, '//*[@placeholder="请输入电站名称"]')
        # 电站联系人输入框
        station_contact_input_loc = (By.XPATH, '//*[@placeholder="请输入电站联系人"]')
        # 电站联系方式
        station_contact_phone_input_loc = (By.XPATH, '//*[@placeholder="请输入电站联系方式"]')
        # 总包单位名称输入框
        total_package_unit_name_input_loc = (By.XPATH, '//*[@placeholder="请输入总包单位名称"]')
        # 我方供货范围输入框
        our_supply_range_input_loc = (By.XPATH, '//*[@placeholder="请输入我方供货范围"]')
        # 质保期起止时间
        warranty_period_start_time_loc = (By.XPATH,)
        # 电站内储能单元分组情况
        station_internal_storage_unit_grouping_situation_loc = (By.XPATH, '//*[@placeholder="请输入电站内储能单元分组情况"]')
        # 电站所属省
        station_belong_province_loc = (By.XPATH, '//*[@placeholder="请输入电站所属省"]')
        # 电站所属市
        station_belong_city_loc = (By.XPATH, '//*[@placeholder="请输入电站所属市"]')
        # 电站所属区/镇
        station_belong_area_loc = (By.XPATH, '//*[@placeholder="请输入电站所属区/镇"]')
        # 经度
        longitude_loc = (By.XPATH, '//*[@placeholder="请输入电站经度"]')
        # 纬度
        latitude_loc = (By.XPATH, '//*[@placeholder="请输入电站纬度"]')

        #===========设备配置信息=============
        # 电池仓数量(个)输入框
        battery_cabinet_number_input_loc = (By.XPATH, '//*[@placeholder="请输入电池仓数量"]')
        # 单台电池仓容量(kWh)输入框
        battery_cabinet_capacity_input_loc = (By.XPATH, '//*[@placeholder="请输入单台电池仓容量(kWh)"]')
        # PCS类型
        pcs_type_select_loc = (By.XPATH, '//*[@class="ant-select-selection-search"]')
        # PCS类型 - 组串式
        pcs_type_group_string_loc = (By.XPATH, '//*[@title="组串式"]')
        # PCS类型 - 集中式
        pcs_type_centralized_loc = (By.XPATH, '//*[@title="集中式"]')
        # pcs类型 -构网型
        pcs_type_grid_loc = (By.XPATH, '//*[@title="构网型"]')
        # PCS一体机数量(个)输入框
        pcs_unit_number_input_loc = (By.XPATH, '//*[@placeholder="请输入PCS一体机数量(个)"]')
        # 电芯材料选择框
        battery_material_select_loc = (By.XPATH, '//*[@class="ant-select-selection-search"]')
        # 电芯材料 - 磷酸铁锂
        battery_material_phosphor_iron_battery_loc = (By.XPATH, '//*[@title="磷酸铁锂"]')
        # 电池堆成组方式输入框
        battery_grouping_method_input_loc = (By.XPATH, '//*[@placeholder="请输入电池堆成组方式"]')
        # 单台PCS最大功率(kW)输入框
        pcs_max_power_input_loc = (By.XPATH, '//*[@placeholder="请输入单台PCS最大功率(kW)"]')
        # 电池簇组成组方式输入框
        battery_cluster_grouping_method_input_loc = (By.XPATH, '//*[@placeholder="请输入电池簇组成组方式"]')
        # 电池模组成组方式输入框
        battery_module_grouping_method_input_loc = (By.XPATH, '//*[@placeholder="请输入电池模组成组方式"]')
        # 单电芯额定容量(Ah)输入框
        single_cell_capacity_input_loc = (By.XPATH, '//*[@placeholder="请输入单电芯额定容量(Ah)"]')
        # 充放电转换效率(%)输入框
        charge_discharge_efficiency_input_loc = (By.XPATH, '//*[@placeholder="请输入充放电转换效率(%)"]')
        # 消防介质输入框
        fire_medium_input_loc = (By.XPATH, '//*[@placeholder="请输入消防介质"]')
        # 额定充放电倍率(C)输入框
        rated_charge_discharge_rate_input_loc = (By.XPATH, '//*[@placeholder="请输入额定充放电倍率(C)"]')
        # 关联电站信息

        #================厂商信息======================
        # BMS厂商选择框
        bms_vendor_select_loc = (By.XPATH, '//*[@placeholder="请输入BMS厂商"]')
        # BMS厂商联系方式输入框
        bms_vendor_contact_phone_input_loc = (By.XPATH, '//*[@placeholder="请输入联系方式"]')

        # PCS厂商选择框
        pcs_vendor_select_loc = (By.XPATH, '//*[@placeholder="请输入PCS厂商"]')
        # PCS厂商联系方式输入框
        pcs_vendor_contact_phone_input_loc = (By.XPATH, '//*[@placeholder="请输入联系方式"]')

        # 变压器厂商选择框
        transformer_vendor_select_loc = (By.XPATH, '//*[@placeholder="请输入变压器厂商"]')
        # 变压器厂商联系方式输入框
        transformer_vendor_contact_phone_input_loc = (By.XPATH, '//*[@placeholder="请输入联系方式"]')

        # 液冷系统厂商选择框
        liquid_cooling_system_vendor_select_loc = (By.XPATH, '//*[@placeholder="请输入液冷系统厂商"]')
        # 液冷系统厂商联系方式输入框
        liquid_cooling_system_vendor_contact_phone_input_loc = (By.XPATH, '//*[@placeholder="请输入联系方式"]')

        # 空调厂商选择框
        air_conditioner_vendor_select_loc = (By.XPATH, '//*[@placeholder="请输入空调厂商"]')
        # 空调厂商联系方式输入框
        air_conditioner_vendor_contact_phone_input_loc = (By.XPATH, '//*[@placeholder="请输入联系方式"]')

        # PACK组装厂厂商选择框
        pack_assembly_vendor_select_loc = (By.XPATH, '//*[@placeholder="请输入PACK组装厂厂商"]')
        # PACK组装厂厂商联系方式输入框
        pack_assembly_vendor_contact_phone_input_loc = (By.XPATH, '//*[@placeholder="请输入联系方式"]')

        # 电芯厂商选择框
        cell_vendor_select_loc = (By.XPATH, '//*[@placeholder="请输入电芯厂商"]')
        # 电芯厂商联系方式输入框
        cell_vendor_contact_phone_input_loc = (By.XPATH, '//*[@placeholder="请输入联系方式"]')

        # 电池仓箱体厂商选择框
        battery_box_vendor_select_loc = (By.XPATH, '//*[@placeholder="请输入电池仓箱体厂商"]')
        # 电池仓箱体厂商联系方式输入框
        battery_box_vendor_contact_phone_input_loc = (By.XPATH, '//*[@placeholder="请输入联系方式"]')

        # 消防厂商选择框
        fire_protection_vendor_select_loc = (By.XPATH, '//*[@placeholder="请输入消防厂商"]')
        # 消防厂商联系方式输入框
        fire_protection_vendor_contact_phone_input_loc = (By.XPATH, '//*[@placeholder="请输入联系方式"]')

        # EMS厂商选择框
        ems_vendor_select_loc = (By.XPATH, '//*[@placeholder="请输入EMS厂商"]')
        # EMS厂商联系方式输入框
        ems_vendor_contact_phone_input_loc = (By.XPATH, '//*[@placeholder="请输入联系方式"]')

        # 汇流柜厂商选择框
        busbar_cabinet_vendor_select_loc = (By.XPATH, '//*[@placeholder="请输入汇流柜厂商"]')
        # 汇流柜厂商联系方式输入框
        busbar_cabinet_vendor_contact_phone_input_loc = (By.XPATH, '//*[@placeholder="请输入联系方式"]')




    # =====================实施维护管理信息=====================
    class ImplementationMaintenanceInfoLocator():
        # 实施计划时间选择框
        implementation_plan_time_select_loc = (By.XPATH, '//*[@class="ant-select-selection-search"]')

        # 实施负责人选择框
        implementation_responsible_select_loc = (By.XPATH, '//*[@class="ant-select-selection-search"]')


    # =====================运维管理信息=====================
    class OperationManagementInfoLocator():
        # 运维负责人选择框
        operation_responsible_select_loc = (By.XPATH, '//*[@class="ant-select-selection-search"]')
        # 首次巡检时间选择框
        first_inspection_time_select_loc = (By.XPATH, '//*[@class="ant-select-selection-search"]')
        # 巡检周期选择框
        inspection_cycle_select_loc = (By.XPATH, '//*[@class="ant-select-selection-search"]')
        # 巡检周期 一个月一次
        inspection_cycle_one_month_loc = (By.XPATH, '//*[@title=" monthly"]')
        # 巡检周期 两个月一次
        inspection_cycle_two_month_loc = (By.XPATH, '//*[@title=" every two months"]')
        # 巡检周期 三个月一次
        inspection_cycle_three_month_loc = (By.XPATH, '//*[@title=" every three months"]')
        # 巡检周期 四个月一次
        inspection_cycle_four_month_loc = (By.XPATH, '//*[@title=" every four months"]')
        # 巡检周期 五个月一次
        inspection_cycle_five_month_loc = (By.XPATH, '//*[@title=" every five months"]')
        # 巡检周期 六个月一次
        inspection_cycle_six_month_loc = (By.XPATH, '//*[@title=" every six months"]')
        # 巡检周期 七个月一次
        inspection_cycle_seven_month_loc = (By.XPATH, '//*[@title=" every seven months"]')
        # 巡检周期 八个月一次
        inspection_cycle_eight_month_loc = (By.XPATH, '//*[@title=" every eight months"]')
        # 巡检周期 九个月一次
        inspection_cycle_nine_month_loc = (By.XPATH, '//*[@title=" every nine months"]')
        # 巡检周期 十个月一次
        inspection_cycle_ten_month_loc = (By.XPATH, '//*[@title=" every ten months"]')
        # 巡检周期 十一个月一次
        inspection_cycle_eleven_month_loc = (By.XPATH, '//*[@title=" every eleven months"]')
        # 巡检周期 十二个月一次
        inspection_cycle_twelve_month_loc = (By.XPATH, '//*[@title=" every twelve months"]')














