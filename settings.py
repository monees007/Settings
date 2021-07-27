#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# written by monees007 on Tue Jul 27 09:08:07 2021
#

import wx

# begin wxGlade: dependencies
# end wxGlade


class Settings(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Settings.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((827, 649))
        self.SetTitle("Settings")

        self.back_panel = wx.Panel(self, wx.ID_ANY)

        view = wx.BoxSizer(wx.VERTICAL)

        self.pane = wx.Notebook(self.back_panel, wx.ID_ANY, style=wx.NB_LEFT)
        self.pane.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.pane.SetForegroundColour(wx.Colour(255, 255, 255))
        view.Add(self.pane, 10, wx.EXPAND, 0)

        self.Watchlist = wx.ScrolledWindow(self.pane, wx.ID_ANY, style=wx.TAB_TRAVERSAL)
        self.Watchlist.SetScrollRate(10, 10)
        self.pane.AddPage(self.Watchlist, "     Watchlist    ")

        sizer_11 = wx.StaticBoxSizer(wx.StaticBox(self.Watchlist, wx.ID_ANY, ""), wx.VERTICAL)

        self.panel_2 = wx.Panel(self.Watchlist, wx.ID_ANY)
        sizer_11.Add(self.panel_2, 1, wx.EXPAND, 0)

        sizer_18 = wx.BoxSizer(wx.VERTICAL)

        sizer_20 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_18.Add(sizer_20, 1, wx.EXPAND, 0)

        self.combo_box_3 = wx.ComboBox(self.panel_2, wx.ID_ANY, choices=["AAVEUSDT", "WAVESUSDT", "CHZUSDT", "BLZUSDT", "# NONE"], style=wx.CB_DROPDOWN | wx.CB_SORT)
        self.combo_box_3.SetSelection(0)
        sizer_20.Add(self.combo_box_3, 2, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 15)

        sizer_20.Add((20, 20), 5, wx.EXPAND, 0)

        timeframe_bar_copy_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_18.Add(timeframe_bar_copy_2, 1, wx.EXPAND, 0)

        timeframe_copy_2 = wx.StaticText(self.panel_2, wx.ID_ANY, "Base Asset ", style=wx.ALIGN_CENTER_HORIZONTAL)
        timeframe_copy_2.SetForegroundColour(wx.Colour(255, 255, 255))
        timeframe_copy_2.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        timeframe_bar_copy_2.Add(timeframe_copy_2, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT | wx.TOP, 15)

        self.text_ctrl_13 = wx.TextCtrl(self.panel_2, wx.ID_ANY, "")
        timeframe_bar_copy_2.Add(self.text_ctrl_13, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 15)

        timeframe_bar_copy_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_18.Add(timeframe_bar_copy_9, 1, wx.EXPAND, 0)

        timeframe_copy_9 = wx.StaticText(self.panel_2, wx.ID_ANY, "Quote Asset", style=wx.ALIGN_CENTER_HORIZONTAL)
        timeframe_copy_9.SetForegroundColour(wx.Colour(255, 255, 255))
        timeframe_copy_9.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        timeframe_bar_copy_9.Add(timeframe_copy_9, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT | wx.TOP, 15)

        self.text_ctrl_20 = wx.TextCtrl(self.panel_2, wx.ID_ANY, "")
        timeframe_bar_copy_9.Add(self.text_ctrl_20, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 15)

        static_line_2 = wx.StaticLine(self.panel_2, wx.ID_ANY)
        static_line_2.SetForegroundColour(wx.Colour(192, 192, 192))
        sizer_18.Add(static_line_2, 0, wx.EXPAND, 0)

        sizer_18.Add((0, 0), 0, 0, 0)

        self.panel_3 = wx.Panel(self.Watchlist, wx.ID_ANY)
        sizer_11.Add(self.panel_3, 1, wx.EXPAND, 0)

        sizer_22 = wx.BoxSizer(wx.VERTICAL)

        sizer_23 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_22.Add(sizer_23, 1, wx.EXPAND, 0)

        self.combo_box_4 = wx.ComboBox(self.panel_3, wx.ID_ANY, choices=["AAVEUSDT", "WAVESUSDT", "CHZUSDT", "BLZUSDT", "# NONE"], style=wx.CB_DROPDOWN | wx.CB_SORT)
        self.combo_box_4.SetSelection(0)
        sizer_23.Add(self.combo_box_4, 2, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 15)

        sizer_23.Add((20, 20), 5, wx.EXPAND, 0)

        timeframe_bar_copy_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_22.Add(timeframe_bar_copy_3, 1, wx.EXPAND, 0)

        timeframe_copy_3 = wx.StaticText(self.panel_3, wx.ID_ANY, "Base Asset ", style=wx.ALIGN_CENTER_HORIZONTAL)
        timeframe_copy_3.SetForegroundColour(wx.Colour(255, 255, 255))
        timeframe_copy_3.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        timeframe_bar_copy_3.Add(timeframe_copy_3, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT | wx.TOP, 15)

        self.text_ctrl_14 = wx.TextCtrl(self.panel_3, wx.ID_ANY, "")
        timeframe_bar_copy_3.Add(self.text_ctrl_14, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 15)

        timeframe_bar_copy_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_22.Add(timeframe_bar_copy_10, 1, wx.EXPAND, 0)

        timeframe_copy_10 = wx.StaticText(self.panel_3, wx.ID_ANY, "Quote Asset", style=wx.ALIGN_CENTER_HORIZONTAL)
        timeframe_copy_10.SetForegroundColour(wx.Colour(255, 255, 255))
        timeframe_copy_10.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        timeframe_bar_copy_10.Add(timeframe_copy_10, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT | wx.TOP, 15)

        self.text_ctrl_21 = wx.TextCtrl(self.panel_3, wx.ID_ANY, "")
        timeframe_bar_copy_10.Add(self.text_ctrl_21, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 15)

        static_line_3 = wx.StaticLine(self.panel_3, wx.ID_ANY)
        sizer_22.Add(static_line_3, 0, wx.EXPAND, 0)

        sizer_22.Add((0, 0), 0, 0, 0)

        self.panel_4 = wx.Panel(self.Watchlist, wx.ID_ANY)
        sizer_11.Add(self.panel_4, 1, wx.EXPAND, 0)

        sizer_24 = wx.BoxSizer(wx.VERTICAL)

        sizer_25 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_24.Add(sizer_25, 1, wx.EXPAND, 0)

        self.combo_box_5 = wx.ComboBox(self.panel_4, wx.ID_ANY, choices=["AAVEUSDT", "WAVESUSDT", "CHZUSDT", "BLZUSDT", "# NONE"], style=wx.CB_DROPDOWN | wx.CB_SORT)
        self.combo_box_5.SetSelection(0)
        sizer_25.Add(self.combo_box_5, 2, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 15)

        sizer_25.Add((20, 20), 5, wx.EXPAND, 0)

        timeframe_bar_copy_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_24.Add(timeframe_bar_copy_5, 1, wx.EXPAND, 0)

        timeframe_copy_5 = wx.StaticText(self.panel_4, wx.ID_ANY, "Base Asset ", style=wx.ALIGN_CENTER_HORIZONTAL)
        timeframe_copy_5.SetForegroundColour(wx.Colour(255, 255, 255))
        timeframe_copy_5.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        timeframe_bar_copy_5.Add(timeframe_copy_5, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT | wx.TOP, 15)

        self.text_ctrl_16 = wx.TextCtrl(self.panel_4, wx.ID_ANY, "")
        timeframe_bar_copy_5.Add(self.text_ctrl_16, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 15)

        timeframe_bar_copy_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_24.Add(timeframe_bar_copy_11, 1, wx.EXPAND, 0)

        timeframe_copy_11 = wx.StaticText(self.panel_4, wx.ID_ANY, "Quote Asset", style=wx.ALIGN_CENTER_HORIZONTAL)
        timeframe_copy_11.SetForegroundColour(wx.Colour(255, 255, 255))
        timeframe_copy_11.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        timeframe_bar_copy_11.Add(timeframe_copy_11, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT | wx.TOP, 15)

        self.text_ctrl_22 = wx.TextCtrl(self.panel_4, wx.ID_ANY, "")
        timeframe_bar_copy_11.Add(self.text_ctrl_22, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 15)

        static_line_4 = wx.StaticLine(self.panel_4, wx.ID_ANY)
        sizer_24.Add(static_line_4, 0, wx.EXPAND, 0)

        sizer_24.Add((0, 0), 0, 0, 0)

        self.panel_1 = wx.Panel(self.Watchlist, wx.ID_ANY)
        sizer_11.Add(self.panel_1, 1, wx.EXPAND, 0)

        sizer_14 = wx.BoxSizer(wx.VERTICAL)

        sizer_16 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_14.Add(sizer_16, 1, wx.EXPAND, 0)

        self.combo_box_2 = wx.ComboBox(self.panel_1, wx.ID_ANY, choices=["AAVEUSDT", "WAVESUSDT", "CHZUSDT", "BLZUSDT", "# NONE"], style=wx.CB_DROPDOWN | wx.CB_SORT)
        self.combo_box_2.SetSelection(0)
        sizer_16.Add(self.combo_box_2, 2, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 15)

        sizer_16.Add((20, 20), 5, wx.EXPAND, 0)

        timeframe_bar_copy_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_14.Add(timeframe_bar_copy_1, 1, wx.EXPAND, 0)

        timeframe_copy_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "Base Asset ", style=wx.ALIGN_CENTER_HORIZONTAL)
        timeframe_copy_1.SetForegroundColour(wx.Colour(255, 255, 255))
        timeframe_copy_1.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        timeframe_bar_copy_1.Add(timeframe_copy_1, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT | wx.TOP, 15)

        self.text_ctrl_12 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        timeframe_bar_copy_1.Add(self.text_ctrl_12, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 15)

        timeframe_bar_copy_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_14.Add(timeframe_bar_copy_8, 1, wx.EXPAND, 0)

        timeframe_copy_8 = wx.StaticText(self.panel_1, wx.ID_ANY, "Quote Asset", style=wx.ALIGN_CENTER_HORIZONTAL)
        timeframe_copy_8.SetForegroundColour(wx.Colour(255, 255, 255))
        timeframe_copy_8.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        timeframe_bar_copy_8.Add(timeframe_copy_8, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT | wx.TOP, 15)

        self.text_ctrl_19 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        timeframe_bar_copy_8.Add(self.text_ctrl_19, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 15)

        static_line_1 = wx.StaticLine(self.panel_1, wx.ID_ANY)
        sizer_14.Add(static_line_1, 0, wx.EXPAND, 0)

        sizer_14.Add((0, 0), 0, 0, 0)

        self.panel_5 = wx.Panel(self.Watchlist, wx.ID_ANY)
        sizer_11.Add(self.panel_5, 1, wx.EXPAND, 0)

        sizer_26 = wx.BoxSizer(wx.VERTICAL)

        sizer_27 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_26.Add(sizer_27, 1, wx.EXPAND, 0)

        self.combo_box_6 = wx.ComboBox(self.panel_5, wx.ID_ANY, choices=["AAVEUSDT", "WAVESUSDT", "CHZUSDT", "BLZUSDT", "# NONE"], style=wx.CB_DROPDOWN | wx.CB_SORT)
        self.combo_box_6.SetSelection(0)
        sizer_27.Add(self.combo_box_6, 2, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 15)

        sizer_27.Add((20, 20), 5, wx.EXPAND, 0)

        timeframe_bar_copy_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_26.Add(timeframe_bar_copy_6, 1, wx.EXPAND, 0)

        timeframe_copy_6 = wx.StaticText(self.panel_5, wx.ID_ANY, "Base Asset ", style=wx.ALIGN_CENTER_HORIZONTAL)
        timeframe_copy_6.SetForegroundColour(wx.Colour(255, 255, 255))
        timeframe_copy_6.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        timeframe_bar_copy_6.Add(timeframe_copy_6, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT | wx.TOP, 15)

        self.text_ctrl_17 = wx.TextCtrl(self.panel_5, wx.ID_ANY, "")
        timeframe_bar_copy_6.Add(self.text_ctrl_17, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 15)

        timeframe_bar_copy_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_26.Add(timeframe_bar_copy_12, 1, wx.EXPAND, 0)

        timeframe_copy_12 = wx.StaticText(self.panel_5, wx.ID_ANY, "Quote Asset", style=wx.ALIGN_CENTER_HORIZONTAL)
        timeframe_copy_12.SetForegroundColour(wx.Colour(255, 255, 255))
        timeframe_copy_12.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        timeframe_bar_copy_12.Add(timeframe_copy_12, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT | wx.TOP, 15)

        self.text_ctrl_23 = wx.TextCtrl(self.panel_5, wx.ID_ANY, "")
        timeframe_bar_copy_12.Add(self.text_ctrl_23, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 15)

        static_line_5 = wx.StaticLine(self.panel_5, wx.ID_ANY)
        sizer_26.Add(static_line_5, 0, wx.EXPAND, 0)

        sizer_26.Add((0, 0), 0, 0, 0)

        sizer_11.Add((0, 0), 0, 0, 0)

        self.Settings = wx.ScrolledWindow(self.pane, wx.ID_ANY, style=wx.TAB_TRAVERSAL)
        self.Settings.SetScrollRate(10, 10)
        self.pane.AddPage(self.Settings, "     Settings     ")

        timeframe_br = wx.StaticBoxSizer(wx.StaticBox(self.Settings, wx.ID_ANY, ""), wx.VERTICAL)

        timeframe_bar = wx.BoxSizer(wx.HORIZONTAL)
        timeframe_br.Add(timeframe_bar, 1, wx.EXPAND, 0)

        lable = wx.BoxSizer(wx.VERTICAL)
        timeframe_bar.Add(lable, 1, wx.EXPAND, 0)

        timeframe = wx.StaticText(self.Settings, wx.ID_ANY, "Time Frame")
        timeframe.SetForegroundColour(wx.Colour(255, 255, 255))
        timeframe.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        lable.Add(timeframe, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 15)

        st1 = wx.StaticText(self.Settings, wx.ID_ANY, "Set the Time Frame")
        lable.Add(st1, 1, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RESERVE_SPACE_EVEN_IF_HIDDEN | wx.RIGHT, 15)

        self.text_ctrl_5 = wx.TextCtrl(self.Settings, wx.ID_ANY, "")
        timeframe_bar.Add(self.text_ctrl_5, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 15)

        ema1_br = wx.BoxSizer(wx.HORIZONTAL)
        timeframe_br.Add(ema1_br, 1, wx.EXPAND, 0)

        sizer_13 = wx.BoxSizer(wx.VERTICAL)
        ema1_br.Add(sizer_13, 1, wx.EXPAND, 0)

        ema1 = wx.StaticText(self.Settings, wx.ID_ANY, "EMA 1")
        ema1.SetForegroundColour(wx.Colour(255, 255, 255))
        ema1.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_13.Add(ema1, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 15)

        st2 = wx.StaticText(self.Settings, wx.ID_ANY, "Set the EMA 1")
        sizer_13.Add(st2, 1, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RESERVE_SPACE_EVEN_IF_HIDDEN | wx.RIGHT, 15)

        self.text_ctrl_6 = wx.TextCtrl(self.Settings, wx.ID_ANY, "")
        ema1_br.Add(self.text_ctrl_6, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 15)

        ema2_br = wx.BoxSizer(wx.HORIZONTAL)
        timeframe_br.Add(ema2_br, 1, wx.EXPAND, 0)

        sizer_15 = wx.BoxSizer(wx.VERTICAL)
        ema2_br.Add(sizer_15, 1, wx.EXPAND, 0)

        ema2 = wx.StaticText(self.Settings, wx.ID_ANY, "EMA 2")
        ema2.SetForegroundColour(wx.Colour(255, 255, 255))
        ema2.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_15.Add(ema2, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 15)

        st3 = wx.StaticText(self.Settings, wx.ID_ANY, "Set the EMA 2")
        sizer_15.Add(st3, 1, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RESERVE_SPACE_EVEN_IF_HIDDEN | wx.RIGHT, 15)

        self.text_ctrl_7 = wx.TextCtrl(self.Settings, wx.ID_ANY, "")
        ema2_br.Add(self.text_ctrl_7, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 15)

        leverage_bar = wx.BoxSizer(wx.HORIZONTAL)
        timeframe_br.Add(leverage_bar, 1, wx.EXPAND, 0)

        sizer_17 = wx.BoxSizer(wx.VERTICAL)
        leverage_bar.Add(sizer_17, 1, wx.EXPAND, 0)

        leverage = wx.StaticText(self.Settings, wx.ID_ANY, "Leverage\n")
        leverage.SetForegroundColour(wx.Colour(255, 255, 255))
        leverage.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_17.Add(leverage, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 15)

        st4 = wx.StaticText(self.Settings, wx.ID_ANY, "Set the Leverage\n")
        sizer_17.Add(st4, 1, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RESERVE_SPACE_EVEN_IF_HIDDEN | wx.RIGHT, 15)

        self.text_ctrl_8 = wx.TextCtrl(self.Settings, wx.ID_ANY, "")
        leverage_bar.Add(self.text_ctrl_8, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 15)

        profitpercent_bar = wx.BoxSizer(wx.HORIZONTAL)
        timeframe_br.Add(profitpercent_bar, 1, wx.EXPAND, 0)

        sizer_19 = wx.BoxSizer(wx.VERTICAL)
        profitpercent_bar.Add(sizer_19, 1, wx.EXPAND, 0)

        profit_percent = wx.StaticText(self.Settings, wx.ID_ANY, "Profit %\n")
        profit_percent.SetForegroundColour(wx.Colour(255, 255, 255))
        profit_percent.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_19.Add(profit_percent, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 15)

        st5 = wx.StaticText(self.Settings, wx.ID_ANY, "Set the Profit Percentage")
        sizer_19.Add(st5, 1, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RESERVE_SPACE_EVEN_IF_HIDDEN | wx.RIGHT, 15)

        self.text_ctrl_9 = wx.TextCtrl(self.Settings, wx.ID_ANY, "")
        profitpercent_bar.Add(self.text_ctrl_9, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 15)

        margin_type_bar = wx.BoxSizer(wx.HORIZONTAL)
        timeframe_br.Add(margin_type_bar, 1, wx.EXPAND, 0)

        sizer_21 = wx.BoxSizer(wx.VERTICAL)
        margin_type_bar.Add(sizer_21, 1, wx.EXPAND, 0)

        margin_type = wx.StaticText(self.Settings, wx.ID_ANY, "Margin Type")
        margin_type.SetForegroundColour(wx.Colour(255, 255, 255))
        margin_type.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_21.Add(margin_type, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 15)

        st6 = wx.StaticText(self.Settings, wx.ID_ANY, "Set the Margin Type")
        sizer_21.Add(st6, 1, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RESERVE_SPACE_EVEN_IF_HIDDEN | wx.RIGHT, 15)

        self.text_ctrl_10 = wx.TextCtrl(self.Settings, wx.ID_ANY, "")
        margin_type_bar.Add(self.text_ctrl_10, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 15)

        exit_sw = wx.BoxSizer(wx.HORIZONTAL)
        timeframe_br.Add(exit_sw, 1, wx.EXPAND, 0)

        lable_copy = wx.BoxSizer(wx.VERTICAL)
        exit_sw.Add(lable_copy, 2, wx.EXPAND, 0)

        exit_tsw = wx.StaticText(self.Settings, wx.ID_ANY, "Exit Switch")
        exit_tsw.SetForegroundColour(wx.Colour(255, 255, 255))
        exit_tsw.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        lable_copy.Add(exit_tsw, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 15)

        st1_copy = wx.StaticText(self.Settings, wx.ID_ANY, "Set the Time Frame")
        lable_copy.Add(st1_copy, 1, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RESERVE_SPACE_EVEN_IF_HIDDEN | wx.RIGHT, 15)

        self.exit_btn = wx.ToggleButton(self.Settings, wx.ID_ANY, "")
        self.exit_btn.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.exit_btn.SetForegroundColour(wx.Colour(0, 0, 0))
        self.exit_btn.SetBitmap(wx.Bitmap("assets/toggle_btn(1).png", wx.BITMAP_TYPE_ANY))
        self.exit_btn.SetBitmapDisabled(wx.Bitmap("assets/toggle_btn(0).png", wx.BITMAP_TYPE_ANY))
        exit_sw.Add(self.exit_btn, 1, wx.BOTTOM | wx.EXPAND | wx.RIGHT | wx.TOP, 28)

        long_sw = wx.BoxSizer(wx.HORIZONTAL)
        timeframe_br.Add(long_sw, 1, wx.EXPAND, 0)

        lable_copy_1 = wx.BoxSizer(wx.VERTICAL)
        long_sw.Add(lable_copy_1, 2, wx.EXPAND, 0)

        long_tsw = wx.StaticText(self.Settings, wx.ID_ANY, "Long Switch")
        long_tsw.SetForegroundColour(wx.Colour(255, 255, 255))
        long_tsw.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        lable_copy_1.Add(long_tsw, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 15)

        st1_copy_1 = wx.StaticText(self.Settings, wx.ID_ANY, "Set the Time Frame")
        lable_copy_1.Add(st1_copy_1, 1, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RESERVE_SPACE_EVEN_IF_HIDDEN | wx.RIGHT, 15)

        self.long_btn = wx.ToggleButton(self.Settings, wx.ID_ANY, "")
        self.long_btn.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.long_btn.SetForegroundColour(wx.Colour(0, 0, 0))
        self.long_btn.SetBitmap(wx.Bitmap("assets/toggle_btn(1).png", wx.BITMAP_TYPE_ANY))
        self.long_btn.SetBitmapDisabled(wx.Bitmap("assets/toggle_btn(0).png", wx.BITMAP_TYPE_ANY))
        long_sw.Add(self.long_btn, 1, wx.BOTTOM | wx.EXPAND | wx.RIGHT | wx.TOP, 28)

        short_sw = wx.BoxSizer(wx.HORIZONTAL)
        timeframe_br.Add(short_sw, 1, wx.EXPAND, 0)

        lable_copy_2 = wx.BoxSizer(wx.VERTICAL)
        short_sw.Add(lable_copy_2, 2, wx.EXPAND, 0)

        short_tsw = wx.StaticText(self.Settings, wx.ID_ANY, "Short Switch")
        short_tsw.SetForegroundColour(wx.Colour(255, 255, 255))
        short_tsw.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        lable_copy_2.Add(short_tsw, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 15)

        st1_copy_2 = wx.StaticText(self.Settings, wx.ID_ANY, "Set the Time Frame")
        lable_copy_2.Add(st1_copy_2, 1, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RESERVE_SPACE_EVEN_IF_HIDDEN | wx.RIGHT, 15)

        self.short_btn = wx.ToggleButton(self.Settings, wx.ID_ANY, "")
        self.short_btn.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.short_btn.SetForegroundColour(wx.Colour(0, 0, 0))
        self.short_btn.SetBitmap(wx.Bitmap("assets/toggle_btn(1).png", wx.BITMAP_TYPE_ANY))
        self.short_btn.SetBitmapDisabled(wx.Bitmap("assets/toggle_btn(0).png", wx.BITMAP_TYPE_ANY))
        short_sw.Add(self.short_btn, 1, wx.BOTTOM | wx.EXPAND | wx.RIGHT | wx.TOP, 28)

        timeframe_br.Add((0, 0), 0, 0, 0)

        self.Credentials = wx.Panel(self.pane, wx.ID_ANY)
        self.pane.AddPage(self.Credentials, "     Credentials     ")

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)

        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)

        webhook_title = wx.StaticText(self.Credentials, wx.ID_ANY, "Webhook URL")
        webhook_title.SetForegroundColour(wx.Colour(255, 255, 255))
        webhook_title.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_4.Add(webhook_title, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 15)

        label_5 = wx.StaticText(self.Credentials, wx.ID_ANY, "Set the Webhook URL")
        sizer_4.Add(label_5, 1, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RESERVE_SPACE_EVEN_IF_HIDDEN | wx.RIGHT, 15)

        self.text_ctrl_1 = wx.TextCtrl(self.Credentials, wx.ID_ANY, "")
        sizer_3.Add(self.text_ctrl_1, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 15)

        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_5, 1, wx.EXPAND, 0)

        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_5.Add(sizer_6, 1, wx.EXPAND, 0)

        label_2 = wx.StaticText(self.Credentials, wx.ID_ANY, "API Key")
        label_2.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_6.Add(label_2, 0, wx.ALL, 15)

        label_6 = wx.StaticText(self.Credentials, wx.ID_ANY, "Set the API Key")
        sizer_6.Add(label_6, 0, wx.BOTTOM | wx.LEFT | wx.RIGHT, 15)

        self.text_ctrl_2 = wx.TextCtrl(self.Credentials, wx.ID_ANY, "")
        sizer_5.Add(self.text_ctrl_2, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 15)

        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_7, 1, wx.EXPAND, 0)

        sizer_8 = wx.BoxSizer(wx.VERTICAL)
        sizer_7.Add(sizer_8, 1, wx.EXPAND, 0)

        label_3 = wx.StaticText(self.Credentials, wx.ID_ANY, "API Secret")
        label_3.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_8.Add(label_3, 0, wx.ALL, 15)

        label_8 = wx.StaticText(self.Credentials, wx.ID_ANY, "Enter the API Secret")
        sizer_8.Add(label_8, 0, wx.BOTTOM | wx.LEFT | wx.RIGHT, 15)

        self.text_ctrl_3 = wx.TextCtrl(self.Credentials, wx.ID_ANY, "")
        sizer_7.Add(self.text_ctrl_3, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 15)

        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_9, 1, wx.EXPAND, 0)

        sizer_10 = wx.BoxSizer(wx.VERTICAL)
        sizer_9.Add(sizer_10, 1, wx.EXPAND, 0)

        label_4 = wx.StaticText(self.Credentials, wx.ID_ANY, "TLD")
        label_4.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_10.Add(label_4, 0, wx.ALL, 15)

        label_7 = wx.StaticText(self.Credentials, wx.ID_ANY, "Set the TLD")
        sizer_10.Add(label_7, 0, wx.BOTTOM | wx.LEFT | wx.RIGHT, 15)

        self.text_ctrl_4 = wx.TextCtrl(self.Credentials, wx.ID_ANY, "")
        sizer_9.Add(self.text_ctrl_4, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 15)

        sizer_1.Add((20, 20), 1, wx.EXPAND, 0)

        self.bottom_bar = wx.Panel(self.back_panel, wx.ID_ANY)
        self.bottom_bar.SetBackgroundColour(wx.Colour(0, 0, 0))
        view.Add(self.bottom_bar, 1, wx.EXPAND, 0)

        sizer_2 = wx.StaticBoxSizer(wx.StaticBox(self.bottom_bar, wx.ID_ANY, ""), wx.HORIZONTAL)

        sizer_2.Add((20, 20), 3, wx.EXPAND, 0)

        btns = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(btns, 2, wx.EXPAND, 0)

        self.save_btn = wx.Button(self.bottom_bar, wx.ID_ANY, "SAVE")
        self.save_btn.SetBackgroundColour(wx.Colour(100, 100, 100))
        self.save_btn.SetForegroundColour(wx.Colour(219, 219, 219))
        btns.Add(self.save_btn, 2, wx.LEFT, 16)

        self.cancel_btn = wx.Button(self.bottom_bar, wx.ID_ANY, "RESET")
        self.cancel_btn.SetBackgroundColour(wx.Colour(100, 100, 100))
        self.cancel_btn.SetForegroundColour(wx.Colour(219, 219, 219))
        btns.Add(self.cancel_btn, 2, wx.LEFT | wx.RIGHT, 16)

        self.bottom_bar.SetSizer(sizer_2)

        self.Credentials.SetSizer(sizer_1)

        self.Settings.SetSizer(timeframe_br)

        self.panel_5.SetSizer(sizer_26)

        self.panel_1.SetSizer(sizer_14)

        self.panel_4.SetSizer(sizer_24)

        self.panel_3.SetSizer(sizer_22)

        self.panel_2.SetSizer(sizer_18)

        self.Watchlist.SetSizer(sizer_11)

        self.back_panel.SetSizer(view)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.save_btn_clicked, self.save_btn)
        self.Bind(wx.EVT_BUTTON, self.reset_btn_clicked, self.cancel_btn)
        # end wxGlade

    def save_btn_clicked(self, event):  # wxGlade: Settings.<event_handler>
        print("Event handler 'save_btn_clicked' not implemented!")
        event.Skip()

    def reset_btn_clicked(self, event):  # wxGlade: Settings.<event_handler>
        print("Event handler 'reset_btn_clicked' not implemented!")
        event.Skip()

# end of class Settings

class MyApp(wx.App):
    def OnInit(self):
        self.frame = Settings(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    settings = MyApp(0)
    settings.MainLoop()
