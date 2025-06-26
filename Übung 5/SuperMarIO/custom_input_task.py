from game_files.custom_actions import post_action, Action

_left_active = False
_right_active = False
_jump_active = False

def custom_input_loop(markerList):
    global _left_active, _right_active, _jump_active

    if markerList is None:
        print("🚫 Keine Person erkannt")
        stop_all_actions()
        return

    lm = markerList.landmark

    # === Sichtbarkeitsprüfung ===
    body_parts = {
        "👣 Linker Fuß (31)": 31,
        "👣 Rechter Fuß (32)": 32,
        "🤚 Linke Hand (15)": 15,
        "🖐 Rechte Hand (16)": 16,
        "🫱 Schulter links (11)": 11,
        "🫲 Schulter rechts (12)": 12
    }

    print("📊 Marker-Sichtbarkeit:")
    for name, idx in body_parts.items():
        vis = lm[idx].visibility
        x, y = lm[idx].x, lm[idx].y
        if vis > 0.5:
            print(f"✅ {name}: sichtbar  | x={x:.2f} y={y:.2f} vis={vis:.2f}")
        else:
            print(f"❌ {name}: unsichtbar | vis={vis:.2f}")

    # === Steuerung mit Füßen ===
    left_foot_ok = lm[31].visibility > 0.5
    right_foot_ok = lm[32].visibility > 0.5

    foot_x = None
    if left_foot_ok and right_foot_ok:
        foot_x = (lm[31].x + lm[32].x) / 2
    elif left_foot_ok:
        foot_x = lm[31].x
    elif right_foot_ok:
        foot_x = lm[32].x

    if foot_x is not None:
        if foot_x < 0.45:
            if not _left_active:
                post_action(Action.LEFT)
                _left_active = True
            if _right_active:
                post_action(Action.RIGHT_STOP)
                _right_active = False
        elif foot_x > 0.55:
            if not _right_active:
                post_action(Action.RIGHT)
                _right_active = True
            if _left_active:
                post_action(Action.LEFT_STOP)
                _left_active = False
        else:
            stop_horizontal_actions()
    else:
        stop_horizontal_actions()

    # === Springen mit Händen über Schulter ===
    hands_ok = lm[15].visibility > 0.5 and lm[16].visibility > 0.5
    shoulders_ok = lm[11].visibility > 0.5 and lm[12].visibility > 0.5

    if hands_ok and shoulders_ok:
        hands_y = (lm[15].y + lm[16].y) / 2
        shoulders_y = (lm[11].y + lm[12].y) / 2

        if hands_y < shoulders_y - 0.02:
            if not _jump_active:
                post_action(Action.JUMP)
                _jump_active = True
        else:
            if _jump_active:
                post_action(Action.JUMP_STOP)
                _jump_active = False
    else:
        if _jump_active:
            post_action(Action.JUMP_STOP)
            _jump_active = False


def stop_all_actions():
    global _left_active, _right_active, _jump_active
    if _left_active:
        post_action(Action.LEFT_STOP)
        _left_active = False
    if _right_active:
        post_action(Action.RIGHT_STOP)
        _right_active = False
    if _jump_active:
        post_action(Action.JUMP_STOP)
        _jump_active = False

def stop_horizontal_actions():
    global _left_active, _right_active
    if _left_active:
        post_action(Action.LEFT_STOP)
        _left_active = False
    if _right_active:
        post_action(Action.RIGHT_STOP)
        _right_active = False
