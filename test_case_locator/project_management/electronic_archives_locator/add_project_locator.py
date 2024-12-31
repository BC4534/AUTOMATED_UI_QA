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
    close_button_loc = (By.XPATH, '(//*[@aria-label="close"])[last()]')
    # 开始时间
    start_time_loc = (By.XPATH, '//*[@placeholder="开始时间"]')
    # 当前月1号 //div[text()=1 and @class="ant-picker-cell-inner"]
    current_month_1_loc = (By.XPATH, '//div[text()="1" and @class="ant-picker-cell-inner"]')
    # 下个月1号
    next_month_1_loc = (By.XPATH, '(//div[text()="1" and @class="ant-picker-cell-inner"])[2]')
    """
    新增项目界面的元素
    由于元素太多了，每个页面再写一个类
    """
    # =====================项目基础资料维护=====================
    class ProjectBaseInfoLocator():
        # 项目基础资料维护界面
        project_base_info_page_loc = (By.XPATH, '//*[text()="项目基础资料维护"]')
        # ===============项目基础资料维护======================
        # 立项时间选择框
        project_time_select_loc = (By.XPATH, '//*[@title="立项时间"]/following::input[@placeholder="请选择日期"]')
        # 立项时间 今天
        project_time_today_loc = (By.XPATH, '//*[text()="今天"]')
        # 项目名称输入框
        project_name_input_loc = (By.XPATH, '(//*[@placeholder="请输入项目名称"])[2]')
        # 项目装机功率输入框
        project_install_power_input_loc = (By.XPATH, '//*[@placeholder="请输入项目装机功率"]')
        # 项目装机容量输入框
        project_install_capacity_input_loc = (By.XPATH, '//*[@placeholder="请输入项目装机容量"]')
        # 项目阶段选择框
        # project_stage_select_loc = (By.XPATH, '(//*[@class="ant-select-selection-search"])[9]')
        # project_stage_select_loc = (By.XPATH, '(//*[text()="请选择项目阶段"])[2]/following::span')
        # project_stage_select_loc = (By.XPATH, '//*[@id="basic_phase"]')
        project_stage_select_loc = (By.XPATH, '//*[@id="basic_phase"]/..')
        # 项目阶段 - 待实施阶段
        project_stage_wait_for_implementation_loc = (By.XPATH, '//*[@title="待实施阶段"]')
        # 项目阶段 - 实施阶段
        project_stage_implementation_loc = (By.XPATH, '//*[@title="实施阶段"]')
        # 项目阶段 - 售后阶段
        project_stage_after_sale_loc = (By.XPATH, '//*[@title="售后阶段"]')
        # 项目进度选择框
        # project_progress_select_loc = (By.XPATH, '(//*[text()="请选择项目进度"])[2]')
        project_progress_select_loc = (By.XPATH, '//*[@id="basic_subPhase"]/..')
        # 项目进度 -计划期
        project_progress_plan_loc = (By.XPATH, '//*[@title="计划期"]')
        # 项目进度 -准备期
        project_progress_preparation_loc = (By.XPATH, '//*[@title="准备期"]')
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
        # project_type_select_loc = (By.XPATH, '(//*[text()="请选择项目类型"])[2]') id="basic_type"
        project_type_select_loc = (By.XPATH, '//*[@id="basic_type"]/..')
        # 项目类型 -工商业
        project_type_commercial_loc = (By.XPATH, '//*[@title="工商业"]')
        # 项目类型 - 电网侧
        project_type_electricity_side_loc = (By.XPATH, '//*[@title="电网侧"]')
        # 项目类型 - 电源侧
        project_type_power_side_loc = (By.XPATH, '//*[@title="电源侧"]')

        # 产品类型
        # product_type_select_loc = (By.XPATH, '(//*[text()="请选择产品类型"])[2]') id="basic_productType"
        product_type_select_loc = (By.XPATH, '//*[@id="basic_productType"]/..')
        # 户外柜文本框值
        product_type_text_loc = (By.XPATH, '//*[@id="basic_productType"]/following::span')
        # 产品类型 - 非系统
        product_type_non_system_loc = (By.XPATH, '//*[@title="非系统"]')
        # 产品类型 - 集装箱
        product_type_container_loc = (By.XPATH, '//*[@title="集装箱"]')
        # 产品类型 - 外户柜
        product_type_outdoor_cabinet_loc = (By.XPATH, '//*[@title="户外柜"]')

        # 所属区域选择框
        # work_order_area_select_loc = (By.XPATH, '//*[text()="请选择所属区域"]') id="basic_region"
        work_order_area_select_loc = (By.XPATH, '//*[@id="basic_region"]/..')

        # 户外柜规格选择框
        outdoor_cabinet_type_select_loc = (By.XPATH, '//*[@id="basic_outdoorCabinetSpec"]/..')
        # 215户外柜国标1.0
        outdoor_cabinet_type_215_gb1_0_loc = (By.XPATH, '//*[@title="215户外柜国标1.0"]')
        # 215户外柜国标2.0
        outdoor_cabinet_type_215_gb2_0_loc = (By.XPATH, '//*[@title="215户外柜国标2.0"]')
        # 232户外柜
        outdoor_cabinet_type_232_loc = (By.XPATH, '//*[@title="232户外柜"]')

        # 所属区域选择框
        project_area_select_loc = (By.XPATH, '//*[@id="basic_region"]/..')
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
        is_support_inspection_standard_yes_loc = (By.XPATH, '//*[@title="是否支持标准巡检"]/following::input[@value="true"]/..')
        # 是否支持巡检标准 - 否
        is_support_inspection_standard_no_loc = (By.XPATH, '//*[@title="是否支持标准巡检"]/following::input[@value="false"]/..')

        # 保存
        save_button_loc = (By.XPATH, '//*[text()="保 存"]')
        # 下一步
        next_button_loc = (By.XPATH, '//*[text()="下一步"]')

        #==============必填项填写=====================
        # 立项时间必填项
        init_time_required_text_loc = (By.XPATH, '//*[@id="basic_approvalTime_help"]/div')
        # 项目名称必填项
        project_name_required_text_loc = (By.XPATH, '//*[@id="basic_name_help"]/div')
        # 项目装机功率必填项
        project_install_power_required_text_loc = (By.XPATH, '//*[@id="basic_maxPowerMw_help"]/div')
        # 项目装机容量必填项
        project_install_capacity_required_text_loc = (By.XPATH, '//*[@id="basic_capacityMwh_help"]/div')
        # 项目阶段必填项
        project_stage_required_text_loc = (By.XPATH, '//*[@id="basic_phase_help"]/div')
        # 项目进度必填项
        project_progress_required_text_loc = (By.XPATH, '//*[@id="basic_subPhase_help"]/div')
        # 项目类型必填项
        project_type_required_text_loc = (By.XPATH, '//*[@id="basic_type_help"]/div')
        # 产品类型必填项
        product_type_required_text_loc = (By.XPATH, '//*[@id="basic_productType_help"]/div')
        # 项目区域必填项
        project_area_required_text_loc = (By.XPATH, '//*[@id="basic_region_help"]/div')
        # 是否支持巡检标准必填项
        is_support_inspection_standard_required_text_loc = (By.XPATH, '//*[@id="basic_supportStandardInspection_help"]/div')





    # =====================项目详细资料维护=====================
    class ProjectDetailInfoLocator():

        # 项目详细资料维护界面
        project_detail_info_page_loc = (By.XPATH, '//*[text()="项目详细资料维护"]')
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
        # 质保期开始时间
        warranty_period_start_time_loc = (By.XPATH, '//*[@placeholder="开始时间"]')
        # 当前月1号 //div[text()=1 and @class="ant-picker-cell-inner"]
        current_month_1_loc = (By.XPATH, '(//div[text()="1" and @class="ant-picker-cell-inner"])[1]')
        # 下个月1号
        next_month_1_loc = (By.XPATH, '(//div[text()="1" and @class="ant-picker-cell-inner"])[2]')



        # 电站内储能单元分组情况
        station_internal_storage_unit_grouping_input_loc = (By.XPATH, '//*[@placeholder="请输入电站内储能单元分组情况"]')
        # 电站所属省
        station_belong_province_input_loc = (By.XPATH, '//*[@placeholder="请输入电站所属省"]')
        # 电站所属市
        station_belong_city_input_loc = (By.XPATH, '//*[@placeholder="请输入电站所属市"]')
        # 电站所属区/镇
        station_belong_area_input_loc = (By.XPATH, '//*[@placeholder="请输入电站所属区/镇"]')
        # 经度
        longitude_input_loc = (By.XPATH, '//*[@placeholder="请输入电站经度"]')
        # 纬度
        latitude_input_loc = (By.XPATH, '//*[@placeholder="请输入电站纬度"]')

        #===========设备配置信息=============
        # 电池仓数量(个)输入框
        battery_cabinet_number_input_loc = (By.XPATH, '//*[@placeholder="请输入电池仓数量"]')
        # 单台电池仓容量(kWh)输入框
        battery_cabinet_capacity_input_loc = (By.XPATH, '//*[@placeholder="请输入单台电池仓容量(kWh)"]')
        # PCS类型 id="basic_pcsType"
        pcs_type_select_loc = (By.XPATH, '//*[@id="basic_pcsType"]/..')
        # pcs_type_select_loc = (By.XPATH, '//*[text()="请选择PCS类型"]/..')
        # PCS类型 - 组串式
        pcs_type_group_string_loc = (By.XPATH, '//*[@title="组串式"]')
        # PCS类型 - 集中式
        pcs_type_centralized_loc = (By.XPATH, '//*[@title="集中式"]')
        # pcs类型 -构网型
        pcs_type_grid_loc = (By.XPATH, '//*[@title="构网型"]')
        # PCS一体机数量(个)输入框
        pcs_unit_number_input_loc = (By.XPATH, '//*[@placeholder="请输入PCS一体机数量"]')
        # 电芯材料选择框 id="basic_cellMaterial"
        battery_material_select_loc = (By.XPATH, '//*[@id="basic_cellMaterial"]/..')
        # battery_material_select_loc = (By.XPATH, '//*[@class="ant-select-selection-search"]')
        # 电芯材料 - 磷酸铁锂
        battery_material_phosphor_iron_battery_loc = (By.XPATH, '//*[@title="磷酸铁锂"]')
        # 电池堆成组方式输入框
        battery_grouping_method_input_loc = (By.XPATH, '//*[@placeholder="请输入电池堆成组方式"]')
        # 单台PCS最大功率(kW)输入框
        pcs_max_power_input_loc = (By.XPATH, '//*[@placeholder="请输入单台PCS最大功率(kW)"]')
        # 电池簇组成组方式输入框
        battery_cluster_grouping_method_input_loc = (By.XPATH, '//*[@placeholder="请输入电池簇成组方式"]')
        # 电池模组成组方式输入框
        battery_module_grouping_method_input_loc = (By.XPATH, '//*[@placeholder="请输入电池模组成组方式"]')
        # 单电芯额定容量(Ah)输入框
        single_cell_capacity_input_loc = (By.XPATH, '//*[@placeholder="请输入单电芯额定容量(Ah)"]')
        # 充放电转换效率(%)输入框
        charge_discharge_efficiency_input_loc = (By.XPATH, '//*[@placeholder="请输入充放电转换效率"]')
        # 消防介质输入框
        fire_medium_input_loc = (By.XPATH, '//*[@placeholder="请输入消防介质"]')
        # 额定充放电倍率(C)输入框
        rated_charge_discharge_rate_input_loc = (By.XPATH, '//*[@placeholder="请输入额定充放电倍率(C)"]')
        # 关联电站信息 id="basic_sePlants"
        associated_station_information_select_loc = (By.XPATH, '//*[@id="basic_sePlants"]/..')
        # 关联电站信息 文本框
        associated_station_information_text_loc = (By.XPATH, '//*[text()="关联电站信息"]')



        #================厂商信息======================
        # BMS厂商选择框 id="basic_BMSManufacturer"
        bms_vendor_select_loc = (By.XPATH, '//*[@id="basic_BMSManufacturer"]/..')
        # BMS厂商联系方式输入框 id="basic_BMSManufacturerPhone"
        bms_vendor_contact_phone_input_loc = (By.XPATH, '//*[@id="basic_BMSManufacturerPhone"]')
        # PCS厂商选择框 id="basic_PCSManufacturer"
        pcs_vendor_select_loc = (By.XPATH, '//*[@id="basic_PCSManufacturer"]/..')
        # PCS厂商联系方式输入框 id="basic_PCSManufacturerPhone"
        pcs_vendor_contact_phone_input_loc = (By.XPATH, '//*[@id="basic_PCSManufacturerPhone"]')
        # 变压器厂商选择框 id="basic_transformerManufacturer"
        transformer_vendor_select_loc = (By.XPATH, '//*[@id="basic_transformerManufacturer"]/..')
        # 变压器厂商联系方式输入框 id="basic_transformerManufacturerPhone"
        transformer_vendor_contact_phone_input_loc = (By.XPATH, '//*[@id="basic_transformerManufacturerPhone"]')
        # 液冷系统厂商选择框 id="basic_liquidCoolingManufacturer"
        liquid_cooling_system_vendor_select_loc = (By.XPATH, '//*[@id="basic_liquidCoolingManufacturer"]/..')
        # 液冷系统厂商联系方式输入框 id="basic_liquidCoolingManufacturerPhone"
        liquid_cooling_system_vendor_contact_phone_input_loc = (By.XPATH, '//*[@id="basic_liquidCoolingManufacturerPhone"]')
        # 空调厂商选择框 id="basic_airManufacturer"
        air_conditioner_vendor_select_loc = (By.XPATH, '//*[@id="basic_airManufacturer"]/..')
        # 空调厂商联系方式输入框 id="basic_airManufacturerPhone"
        air_conditioner_vendor_contact_phone_input_loc = (By.XPATH, '//*[@id="basic_airManufacturerPhone"]')
        # PACK组装厂厂商选择框 id="basic_PACKManufacturer"
        pack_assembly_vendor_select_loc = (By.XPATH, '//*[@id="basic_PACKManufacturer"]/..')
        # PACK组装厂厂商联系方式输入框 id="basic_PACKManufacturerPhone"
        pack_assembly_vendor_contact_phone_input_loc = (By.XPATH, '//*[@id="basic_PACKManufacturerPhone"]')
        # 电芯厂商选择框 id="basic_cellManufacturer"
        cell_vendor_select_loc = (By.XPATH, '//*[@id="basic_cellManufacturer"]/..')
        # 电芯厂商联系方式输入框 id="basic_cellManufacturerPhone"
        cell_vendor_contact_phone_input_loc = (By.XPATH, '//*[@id="basic_cellManufacturerPhone"]')
        # 电池仓箱体厂商选择框 id="basic_batteryManufacturer"
        battery_box_vendor_select_loc = (By.XPATH, '//*[@id="basic_batteryManufacturer"]/..')
        # 电池仓箱体厂商联系方式输入框 id="basic_batteryManufacturerPhone"
        battery_box_vendor_contact_phone_input_loc = (By.XPATH, '//*[@id="basic_batteryManufacturerPhone"]')
        # 消防厂商选择框 id="basic_fireManufacturer"
        fire_protection_vendor_select_loc = (By.XPATH, '//*[@id="basic_fireManufacturer"]/..')
        # 消防厂商联系方式输入框 id="basic_fireManufacturerPhone"
        fire_protection_vendor_contact_phone_input_loc = (By.XPATH, '//*[@id="basic_fireManufacturerPhone"]')
        # EMS厂商选择框 id="basic_emsManufacturer"
        ems_vendor_select_loc = (By.XPATH, '//*[@id="basic_emsManufacturer"]/..')
        # EMS厂商联系方式输入框 id="basic_emsManufacturerPhone"
        ems_vendor_contact_phone_input_loc = (By.XPATH, '//*[@id="basic_emsManufacturerPhone"]')
        # 汇流柜厂商选择框 id="basic_combinerCabinetManufacturer"
        busbar_cabinet_vendor_select_loc = (By.XPATH, '//*[@id="basic_combinerCabinetManufacturer"]/..')
        # 汇流柜厂商联系方式输入框 id="basic_combinerCabinetManufacturerPhone"
        busbar_cabinet_vendor_contact_phone_input_loc = (By.XPATH, '//*[@id="basic_combinerCabinetManufacturerPhone"]')

        # ===============必填项
        # 业主名称 id="basic_ownerName_help"
        owner_required_loc = (By.XPATH, '//*[@id="basic_ownerName_help"]/div')
        # 电池仓个数必填项 id="basic_batterySlotCount_help"
        battery_box_number_required_loc = (By.XPATH, '//*[@id="basic_batterySlotCount_help"]/div')
        # bms厂商 id="basic_BMSManufacturer_help"
        bms_vendor_required_loc = (By.XPATH, '//*[@id="basic_BMSManufacturer_help"]/div')




    # =====================实施维护管理信息=====================
    class ImplementationMaintenanceInfoLocator():
        # // *[text() = "维护实施管理信息"]维护实施管理信息
        maintain_implement_info_management_page_loc =  (By.XPATH, '//*[text() = "维护实施管理信息"]')
        # 实施计划时间选择框 id="basic_implementationPlanTime"
        implementation_plan_time_loc = (By.XPATH, '//*[@id="basic_implementationPlanTime"]/..')


        # 实施负责人选择框 id="basic_implementManagerAccount"
        implementation_responsible_select_loc = (By.XPATH, '//*[@id="basic_implementManagerAccount"]/..')
        # 实施负责人 - 系统管理员
        implementation_responsible_system_administrator_loc = (By.XPATH, '//*[@class="rc-virtual-list-holder-inner"]/div[@title="系统管理员"]')


        # 实施负责人后面的（！）
        implementation_responsible_tip_loc = (By.XPATH, '//*[text()="实施负责人"]')
        # 实施负责人！的提示文本
        implementation_responsible_tip_text_loc = (By.XPATH, '//*[text()="创建项目后，会在计划开始时间时自动创建一条实施工单至实施负责人，实施阶段该项目 产生的所有工单会由实施负责人负责。"]')

        # ===============必填项
        # 请输入实施计划时间 id="basic_implementationPlanTime_help"
        implementation_plan_time_required_loc = (By.XPATH, '//*[@id="basic_implementationPlanTime_help"]/div')
        # 请选择实施负责人
        implementation_responsible_required_loc = (By.XPATH, '//*[text()="请选择实施负责人"]')


    # =====================运维管理信息=====================
    class OperationManagementInfoLocator():
        # 运维管理界面
        operation_management_info_page_loc =  (By.XPATH, '//*[text() = "运维管理信息"]')
        # 运维负责人选择框 id="basic_operationsManagerAccount"
        operation_responsible_select_loc = (By.XPATH, '//*[@id="basic_operationsManagerAccount"]/..')
        # 运维负责人 - 系统管理员
        operation_responsible_system_administrator_loc = (By.XPATH, '//*[@class="rc-virtual-list-holder-inner"]/div[@title="系统管理员"]')
        # 运维负责人后面的（！）
        operation_responsible_tip_loc = (By.XPATH, '//*[text()="运维负责人"]')
        # 运维负责人！的提示文本
        operation_responsible_tip_text_loc = (By.XPATH, '//*[text()="创建项目后，实施阶段该项目产生的所有工单将由实施负责人处理。"]')
        # 首次巡检时间选择框 id="basic_firstInspectionDate
        first_inspection_time_select_loc = (By.XPATH, '//*[@id="basic_firstInspectionDate"]/..')
        # 今天
        first_inspection_time_today_loc = (By.XPATH, '//*[text()="今天"]')
        # 下一个月按钮 //*[@class="ant-picker-next-icon"]/..
        next_month_button_loc = (By.XPATH, '//*[@class="ant-picker-header-next-btn"]')
        # 1号
        first_day_loc = (By.XPATH, '//tbody/following::div[text()="1"]')
        # 巡检周期选择框 id="basic_inspectionCycle"
        inspection_cycle_select_loc = (By.XPATH, '//*[@id="basic_inspectionCycle"]/..')
        # 巡检周期 一个月一次
        inspection_cycle_one_month_loc = (By.XPATH, '//*[@title="一月一次"]')
        # 巡检周期 两个月一次
        inspection_cycle_two_month_loc = (By.XPATH, '//*[@title="二月一次"]')
        # 巡检周期 三个月一次
        inspection_cycle_three_month_loc = (By.XPATH, '//*[@title="三月一次"]')
        # 巡检周期 四个月一次
        inspection_cycle_four_month_loc = (By.XPATH, '//*[@title="四月一次"]')
        # 巡检周期 五个月一次
        inspection_cycle_five_month_loc = (By.XPATH, '//*[@title="五月一次"]')
        # 巡检周期 六个月一次
        inspection_cycle_six_month_loc = (By.XPATH, '//*[@title="六月一次"]')
        # 巡检周期 七个月一次
        inspection_cycle_seven_month_loc = (By.XPATH, '//*[@title="七月一次"]')
        # 巡检周期 八个月一次
        inspection_cycle_eight_month_loc = (By.XPATH, '//*[@title="八月一次"]')
        # 巡检周期 九个月一次
        inspection_cycle_nine_month_loc = (By.XPATH, '//*[@title="九月一次"]')
        # 巡检周期 十个月一次
        inspection_cycle_ten_month_loc = (By.XPATH, '//*[@title="十月一次"]')
        # 巡检周期 十一个月一次
        inspection_cycle_eleven_month_loc = (By.XPATH, '//*[@title="十一月一次"]')
        # 巡检周期 十二个月一次
        inspection_cycle_twelve_month_loc = (By.XPATH, '//*[@title="十二月一次"]')

        # 添加巡检组
        add_inspection_group_button_loc = (By.XPATH, '//*[text()="添加巡检组"]/..')

        # 输入巡检组名
        inspection_group_name_input_loc = (By.XPATH, '//*[@id="basic_inspectionGroups_0_nameLabel"]')

        # 点击添加巡检项按钮
        add_inspection_item_button_loc = (By.XPATH, '//*[text()="添加巡检事项"]/..')
        # 巡检项1选择框 id="basic_inspectionGroups_0_inspectionTeamGroup_0_inspectionItemIds"
        inspection_item_select_loc = (By.XPATH, '//*[@id="basic_inspectionGroups_0_inspectionTeamGroup_0_inspectionItemIds"]/..')

        # 第一个巡检项
        inspection_item_one_loc = (By.XPATH, '(//*[@class="rc-virtual-list-holder-inner"])[3]/div/div')

        # 批量下载巡检编码按钮
        batch_download_inspection_code_button_loc = (By.XPATH, '//*[text()="批量下载巡检编码"]/..')

        # ==================比填项
        # 请选择运维负责人 id="basic_operationsManagerAccount_help"
        operation_responsible_required_text_loc = (By.XPATH, '//*[@id="basic_operationsManagerAccount_help"]/div')
        # 请选择首次巡检时间 id="basic_firstInspectionDate_help"
        first_inspection_time_required_text_loc = (By.XPATH, '//*[@id="basic_firstInspectionDate_help"]/div')
        # 请选择巡检周期 id="basic_inspectionCycle_help"
        inspection_cycle_required_text_loc = (By.XPATH, '//*[@id="basic_inspectionCycle_help"]/div')








ProjectBaseInfoLocator = AddProjectLocator().ProjectBaseInfoLocator()
ProjectDetailInfoLocator = AddProjectLocator().ProjectDetailInfoLocator()
ImplementationMaintenanceInfoLocator = AddProjectLocator().ImplementationMaintenanceInfoLocator()
OperationManagementInfoLocator = AddProjectLocator().OperationManagementInfoLocator()
__all__ = ["AddProjectLocator", "ProjectBaseInfoLocator", "ProjectDetailInfoLocator", "ImplementationMaintenanceInfoLocator", "OperationManagementInfoLocator"]

















