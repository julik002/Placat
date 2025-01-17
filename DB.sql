PGDMP      &                |            Posters    16.1    16.1     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    35363    Posters    DATABASE     }   CREATE DATABASE "Posters" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE "Posters";
                postgres    false            �            1259    35374    posters    TABLE     ;  CREATE TABLE public.posters (
    number integer NOT NULL,
    code text NOT NULL,
    publishing_house text NOT NULL,
    year integer NOT NULL,
    topic text NOT NULL,
    series text NOT NULL,
    name text,
    format text,
    orientation text,
    link_to_the_photo text,
    note_1 text,
    note_2 text
);
    DROP TABLE public.posters;
       public         heap    postgres    false            �          0    35374    posters 
   TABLE DATA           �   COPY public.posters (number, code, publishing_house, year, topic, series, name, format, orientation, link_to_the_photo, note_1, note_2) FROM stdin;
    public          postgres    false    215   i       P           2606    35380    posters Posters_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.posters
    ADD CONSTRAINT "Posters_pkey" PRIMARY KEY (number);
 @   ALTER TABLE ONLY public.posters DROP CONSTRAINT "Posters_pkey";
       public            postgres    false    215            �     x��\KoG>S�b�S�>E�ǽ�/�)�䘳�Ñ�x!8�+��e��XI�B�?���zzݤF�P���M�{������;u���~}��6�G�{j�Fj�U����D�@����5l��fC]�0>Tj�'��f�<����Ǘ�������c���#!�}��.��R��A]�|1��C���������z꒾��k(,r������!�OW ��e�n{���><�,̵f�c ��p���o�X��a��[D�?�B�Lͅ���;�� ����@��S�D�!�8�^�}DJ&I 6RL���i��h���i�ad��s|��oh��w�S�3U�����~�2q�#�F~j��ʳ�������R<K/n7�2>�|�j��V�O�����ӧv�|a���Q���XE���Y[~"���#��m+=ʅ��B������k�� -R�D�z,3G1j�]�Ǝ�ϱ��?���M�'����F�]?�{&d|�A��&���^��mm܇V�����̾s���x�Q/�Y`�}8�$#��&��]� �D���I�fy|h�߼��~a� |S�|�:g��B���J)p%`'������y׸�o�Q8���2�A��	�|��ko���C��x3�9��	��ρ�q�dd���-�/9�`n�-��x �Xtd챮p�dM���X�����3����d��`�����:�����&��d��ټ�['�����=� ��֩!���x8�N�0,O��y���QM�%�B�h����<�����|��<��f�2�)�C�+vx��	��%9zd����#Z1|�%͹9-�ܑL��x&=]�#| �p{��k4	�P�˪͡�J����p)f��g�$i�h?瀝�})�v%:�L��gkK��������­��F�`?Z�?D�#� �E�#'	,٩�e|Q)\���[�uO#�T )HQ }�gC�z&\0��>dKO~��8�?x�*��K3�y���O�Ȳ�_
np��@䄤���hkƙ��w��{��F�Fc�S��������9䏐��ԋ�$=M_���5�+Q�g��G�	XecV���梺�@gByՃ{/9<�*�a�*��g���5
�9@O#&=V����3!�/�e�+�\�@x�ƈ��������	` 'L�8م7����g���~<�0$��`Z��b�pE�����)X��;����R����JF\�;�e��v/%,����k���4�L&ȲP�P��ܮ�츬��a
� _��|k�n��H/G���S@����1�T	����:�<2]���1ҫs;s���c߸t���Fk
�.2�Z2���A/��|KW�mN_?�aK�Qf��V���/A7E�lYǔ�7����䑤%F��X�D�������`��^�7�P��\�����>�ڔ_�<g��;d	��4�=a=,�ލ���u���]4b�\sK���.�
9��τ8	�"]�Ϻ�{kv��Q�b�UC�B���-��rp�������	�[݋9�����2�ੲJ|�ܗFv�ŀ�5����x���Ϩˡ�	wUpb��u�f����9#�b��˜=R�gɼJ��Cg>���E���nU5���K��hW���L�+O�\����3�~2'`$� ���G ���ϭ��dy�f�6���ȴk���o�}�V��[WVlв�f�o��Ƽ�2;�t�-���_���k���:k���w��X���k���* *l��Z�H�/,�=߱�����-Y�/��rM���O	�Wԣ�NDεЙK�}��YAk��T�U�r,�ߴ��Ҕz�h�(�	���H�r-v�9��v�7�O��Yh|#G6������r�cNy�;������l��S3�7:�q�3�� ���'ױ�>��y�.y�d_Dr.�l4��r>��b{Qqΰg�;��9�e,�zG�|�����RU��ks�G���;6K��)�6<��E�C��.'���Q̚�l}�xl�پ�R�;6\_)����0i�+�����m�]���F�E�̥�~�J��
j���L�AN��j5�T�5�����4��*}d�HSz�82�E�r����X�\O��y���d�(bv������{$��]U�����WczG�[��O0]g�U��J���ev���v�\v��`�][���DQf]$=��8��0�Z��Z�h�3;i����:Ub�8+JAŁ��	�\�,�˼������ �l�����Cr������<�t��lS$�}�~��j~q��v����$�L�`�z��$}�v|�
X�YF١T_�Ј0��b���N�p_���Ι:�	�����LXT#S����אS/q(�8��^f������a��0��VH9�����U"wHd$�sRd�Lle	��ٮ��TN7$K�{��}X�	ƟF�lBg�D��]�k�Ӽ�c^�B�w'�'�9�tj��.2��)R΃����>9����4�\�͠W��0K.ӄzǛ�Ӗ����`ۧ9ѯO�7�AF��0[�	J��8��}�:h�:=��wj��eKv�@Jn�j���|��U�V�Y��W�az��0݃�&��j��=�r��ڈHsG��c,u�x-��\�mZZ���_^�\�ߒ�Ȱ;vG��i}^ӥ���K��\Y�'���5϶F�w�
�J���ҭf�>-g^�J9?�լѧ�&�u����+{��5:2sԻu��R��t�������߅��Yja�>�0�?�1�s��3z,��;�5=\��^G[[5Ɣ���~K&U�������Oś|�������.�$f�n�&a�,V�U�;.�9��2T�-yc�t�KrO|�N�����z\�}�%�Ϛe* O���1.�т��doi&�� ֮х��lZM6���V��@�P��Meɜy_�zaɸ_��w�R�-�.p'����)'^����kp֟��9��]���޼��?�uِ��-|�{��O��H���i��<yc�K�+s˖�iO�a/��|�R7cx�Ʒ_}�u�5��K��� דF��E������^����?�lp�     