#866 - строка
sp, hgh, krn, rsk = self.calc1.Sig_Calculate(self.dx, self.dy)
#delta_time-время опроса/время кадра
#dx и dy сделать как отношение координаты по камере к расстоянию до цели(угол)
#для контроля  скорости сближения необходимо добавить dv-ошибку по скорости, которая будет регулироваться тангажом