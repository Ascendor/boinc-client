from marshmallow import Schema, fields


class GlobalPreferenceOverride(Schema):
    confirm_before_connecting = fields.Int()
    cpu_scheduling_period_minutes = fields.Float()
    cpu_usage_limit = fields.Float()
    daily_xfer_limit_mb = fields.Float()
    daily_xfer_period_days = fields.Int()
    disk_interval = fields.Float()
    disk_max_used_gb = fields.Float()
    disk_max_used_pct = fields.Float()
    disk_min_free_gb = fields.Float()
    dont_verify_images = fields.Int()
    end_hour = fields.Float()
    hangup_if_dialed = fields.Int()
    idle_time_to_run = fields.Float()
    leave_apps_in_memory = fields.Int()
    max_bytes_sec_down = fields.Float()
    max_bytes_sec_up = fields.Float()
    max_ncpus_pct = fields.Float()
    net_end_hour = fields.Float()
    net_start_hour = fields.Float()
    ram_max_used_busy_pct = fields.Float()
    ram_max_used_idle_pct = fields.Float()
    run_gpu_if_user_active = fields.Int()
    run_if_user_active = fields.Int()
    run_on_batteries = fields.Int()
    start_hour = fields.Float()
    suspend_cpu_usage = fields.Float()
    suspend_if_no_recent_input = fields.Float()
    vm_max_used_pct = fields.Float()
    work_buf_additional_days = fields.Float()
    work_buf_min_days = fields.Float()


class GlobalPreferenceOverrides(Schema):
    global_preferences = fields.Nested(GlobalPreferenceOverride())
