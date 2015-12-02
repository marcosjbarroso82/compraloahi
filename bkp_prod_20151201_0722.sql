--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: account_emailaddress; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE account_emailaddress (
    id integer NOT NULL,
    email character varying(254) NOT NULL,
    verified boolean NOT NULL,
    "primary" boolean NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.account_emailaddress OWNER TO compraloahi;

--
-- Name: account_emailaddress_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE account_emailaddress_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_emailaddress_id_seq OWNER TO compraloahi;

--
-- Name: account_emailaddress_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE account_emailaddress_id_seq OWNED BY account_emailaddress.id;


--
-- Name: account_emailconfirmation; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE account_emailconfirmation (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    sent timestamp with time zone,
    key character varying(64) NOT NULL,
    email_address_id integer NOT NULL
);


ALTER TABLE public.account_emailconfirmation OWNER TO compraloahi;

--
-- Name: account_emailconfirmation_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE account_emailconfirmation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_emailconfirmation_id_seq OWNER TO compraloahi;

--
-- Name: account_emailconfirmation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE account_emailconfirmation_id_seq OWNED BY account_emailconfirmation.id;


--
-- Name: adLocation_adlocation; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE "adLocation_adlocation" (
    id integer NOT NULL,
    title character varying(40) NOT NULL,
    lat double precision NOT NULL,
    lng double precision NOT NULL,
    address json NOT NULL,
    ad_id integer NOT NULL
);


ALTER TABLE public."adLocation_adlocation" OWNER TO compraloahi;

--
-- Name: adLocation_adlocation_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE "adLocation_adlocation_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."adLocation_adlocation_id_seq" OWNER TO compraloahi;

--
-- Name: adLocation_adlocation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE "adLocation_adlocation_id_seq" OWNED BY "adLocation_adlocation".id;


--
-- Name: ad_ad; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE ad_ad (
    id integer NOT NULL,
    title character varying(40) NOT NULL,
    body text NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    pub_date timestamp with time zone NOT NULL,
    slug character varying(50) NOT NULL,
    published boolean NOT NULL,
    status integer NOT NULL,
    short_description character varying(100) NOT NULL,
    price numeric(10,2) NOT NULL,
    store_published boolean NOT NULL,
    author_id integer NOT NULL
);


ALTER TABLE public.ad_ad OWNER TO compraloahi;

--
-- Name: ad_ad_categories; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE ad_ad_categories (
    id integer NOT NULL,
    ad_id integer NOT NULL,
    category_id integer NOT NULL
);


ALTER TABLE public.ad_ad_categories OWNER TO compraloahi;

--
-- Name: ad_ad_categories_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE ad_ad_categories_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ad_ad_categories_id_seq OWNER TO compraloahi;

--
-- Name: ad_ad_categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE ad_ad_categories_id_seq OWNED BY ad_ad_categories.id;


--
-- Name: ad_ad_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE ad_ad_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ad_ad_id_seq OWNER TO compraloahi;

--
-- Name: ad_ad_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE ad_ad_id_seq OWNED BY ad_ad.id;


--
-- Name: ad_adimage; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE ad_adimage (
    id integer NOT NULL,
    image character varying(100) NOT NULL,
    "default" boolean NOT NULL,
    ad_id_id integer NOT NULL
);


ALTER TABLE public.ad_adimage OWNER TO compraloahi;

--
-- Name: ad_adimage_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE ad_adimage_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ad_adimage_id_seq OWNER TO compraloahi;

--
-- Name: ad_adimage_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE ad_adimage_id_seq OWNED BY ad_adimage.id;


--
-- Name: ad_category; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE ad_category (
    id integer NOT NULL,
    name character varying(40) NOT NULL,
    slug character varying(50) NOT NULL
);


ALTER TABLE public.ad_category OWNER TO compraloahi;

--
-- Name: ad_category_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE ad_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ad_category_id_seq OWNER TO compraloahi;

--
-- Name: ad_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE ad_category_id_seq OWNED BY ad_category.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO compraloahi;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO compraloahi;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO compraloahi;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO compraloahi;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO compraloahi;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO compraloahi;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO compraloahi;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO compraloahi;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO compraloahi;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO compraloahi;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO compraloahi;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO compraloahi;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: authtoken_token; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE authtoken_token (
    key character varying(40) NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.authtoken_token OWNER TO compraloahi;

--
-- Name: corsheaders_corsmodel; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE corsheaders_corsmodel (
    id integer NOT NULL,
    cors character varying(255) NOT NULL
);


ALTER TABLE public.corsheaders_corsmodel OWNER TO compraloahi;

--
-- Name: corsheaders_corsmodel_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE corsheaders_corsmodel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.corsheaders_corsmodel_id_seq OWNER TO compraloahi;

--
-- Name: corsheaders_corsmodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE corsheaders_corsmodel_id_seq OWNED BY corsheaders_corsmodel.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO compraloahi;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO compraloahi;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_comment_flags; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE django_comment_flags (
    id integer NOT NULL,
    flag character varying(30) NOT NULL,
    flag_date timestamp with time zone NOT NULL,
    comment_id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.django_comment_flags OWNER TO compraloahi;

--
-- Name: django_comment_flags_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE django_comment_flags_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_comment_flags_id_seq OWNER TO compraloahi;

--
-- Name: django_comment_flags_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE django_comment_flags_id_seq OWNED BY django_comment_flags.id;


--
-- Name: django_comments; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE django_comments (
    id integer NOT NULL,
    object_pk text NOT NULL,
    user_name character varying(50) NOT NULL,
    user_email character varying(254) NOT NULL,
    user_url character varying(200) NOT NULL,
    comment text NOT NULL,
    submit_date timestamp with time zone NOT NULL,
    ip_address inet,
    is_public boolean NOT NULL,
    is_removed boolean NOT NULL,
    content_type_id integer NOT NULL,
    site_id integer NOT NULL,
    user_id integer
);


ALTER TABLE public.django_comments OWNER TO compraloahi;

--
-- Name: django_comments_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE django_comments_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_comments_id_seq OWNER TO compraloahi;

--
-- Name: django_comments_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE django_comments_id_seq OWNED BY django_comments.id;


--
-- Name: django_comments_xtd_xtdcomment; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE django_comments_xtd_xtdcomment (
    comment_ptr_id integer NOT NULL,
    thread_id integer NOT NULL,
    parent_id integer NOT NULL,
    level smallint NOT NULL,
    "order" integer NOT NULL,
    followup boolean NOT NULL
);


ALTER TABLE public.django_comments_xtd_xtdcomment OWNER TO compraloahi;

--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO compraloahi;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO compraloahi;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO compraloahi;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO compraloahi;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO compraloahi;

--
-- Name: django_site; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.django_site OWNER TO compraloahi;

--
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE django_site_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_site_id_seq OWNER TO compraloahi;

--
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE django_site_id_seq OWNED BY django_site.id;


--
-- Name: djmail_message; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE djmail_message (
    uuid character varying(40) NOT NULL,
    from_email character varying(1024) NOT NULL,
    to_email text NOT NULL,
    body_text text NOT NULL,
    body_html text NOT NULL,
    subject character varying(1024) NOT NULL,
    data text NOT NULL,
    retry_count smallint NOT NULL,
    status smallint NOT NULL,
    priority smallint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    sent_at timestamp with time zone,
    exception text NOT NULL
);


ALTER TABLE public.djmail_message OWNER TO compraloahi;

--
-- Name: faq_question; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE faq_question (
    id integer NOT NULL,
    text text NOT NULL,
    answer text NOT NULL,
    slug character varying(100) NOT NULL,
    status integer NOT NULL,
    protected boolean NOT NULL,
    sort_order integer NOT NULL,
    created_on timestamp with time zone NOT NULL,
    updated_on timestamp with time zone NOT NULL,
    nr_views integer NOT NULL,
    created_by_id integer,
    topic_id integer NOT NULL,
    updated_by_id integer
);


ALTER TABLE public.faq_question OWNER TO compraloahi;

--
-- Name: faq_question_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE faq_question_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.faq_question_id_seq OWNER TO compraloahi;

--
-- Name: faq_question_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE faq_question_id_seq OWNED BY faq_question.id;


--
-- Name: faq_questionscore; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE faq_questionscore (
    id integer NOT NULL,
    score integer NOT NULL,
    ip_address inet,
    question_id integer NOT NULL,
    user_id integer
);


ALTER TABLE public.faq_questionscore OWNER TO compraloahi;

--
-- Name: faq_questionscore_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE faq_questionscore_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.faq_questionscore_id_seq OWNER TO compraloahi;

--
-- Name: faq_questionscore_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE faq_questionscore_id_seq OWNED BY faq_questionscore.id;


--
-- Name: faq_topic; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE faq_topic (
    id integer NOT NULL,
    name character varying(150) NOT NULL,
    slug character varying(150) NOT NULL,
    sort_order integer NOT NULL,
    nr_views integer NOT NULL,
    icon character varying(100),
    created_on timestamp with time zone NOT NULL,
    updated_on timestamp with time zone NOT NULL,
    description character varying(255) NOT NULL,
    created_by_id integer,
    site_id integer,
    updated_by_id integer
);


ALTER TABLE public.faq_topic OWNER TO compraloahi;

--
-- Name: faq_topic_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE faq_topic_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.faq_topic_id_seq OWNER TO compraloahi;

--
-- Name: faq_topic_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE faq_topic_id_seq OWNED BY faq_topic.id;


--
-- Name: favorite_favorite; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE favorite_favorite (
    id integer NOT NULL,
    target_object_id integer NOT NULL,
    "timestamp" timestamp with time zone NOT NULL,
    target_content_type_id integer NOT NULL,
    user_id integer NOT NULL,
    CONSTRAINT favorite_favorite_target_object_id_check CHECK ((target_object_id >= 0))
);


ALTER TABLE public.favorite_favorite OWNER TO compraloahi;

--
-- Name: favorite_favorite_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE favorite_favorite_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.favorite_favorite_id_seq OWNER TO compraloahi;

--
-- Name: favorite_favorite_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE favorite_favorite_id_seq OWNED BY favorite_favorite.id;


--
-- Name: msg_msg; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE msg_msg (
    id integer NOT NULL,
    subject character varying(30) NOT NULL,
    body text NOT NULL,
    sent_at timestamp with time zone NOT NULL,
    read_at timestamp with time zone,
    replied_at timestamp with time zone,
    sender_archived boolean NOT NULL,
    recipient_archived boolean NOT NULL,
    sender_deleted_at timestamp with time zone,
    recipient_deleted_at timestamp with time zone,
    moderation_status character varying(1) NOT NULL,
    moderation_date timestamp with time zone,
    moderation_reason character varying(120) NOT NULL,
    object_id integer,
    content_type_id integer,
    parent_id integer,
    recipient_id integer,
    sender_id integer,
    thread_id integer,
    CONSTRAINT msg_msg_object_id_check CHECK ((object_id >= 0))
);


ALTER TABLE public.msg_msg OWNER TO compraloahi;

--
-- Name: msg_msg_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE msg_msg_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.msg_msg_id_seq OWNER TO compraloahi;

--
-- Name: msg_msg_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE msg_msg_id_seq OWNED BY msg_msg.id;


--
-- Name: notification_confignotification; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE notification_confignotification (
    id integer NOT NULL,
    config json NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.notification_confignotification OWNER TO compraloahi;

--
-- Name: notification_confignotification_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE notification_confignotification_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.notification_confignotification_id_seq OWNER TO compraloahi;

--
-- Name: notification_confignotification_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE notification_confignotification_id_seq OWNED BY notification_confignotification.id;


--
-- Name: notification_notification; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE notification_notification (
    id integer NOT NULL,
    type character varying(20) NOT NULL,
    message text NOT NULL,
    created timestamp with time zone NOT NULL,
    extras json NOT NULL,
    read timestamp with time zone,
    receiver_id integer NOT NULL
);


ALTER TABLE public.notification_notification OWNER TO compraloahi;

--
-- Name: notification_notification_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE notification_notification_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.notification_notification_id_seq OWNER TO compraloahi;

--
-- Name: notification_notification_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE notification_notification_id_seq OWNED BY notification_notification.id;


--
-- Name: push_notifications_apnsdevice; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE push_notifications_apnsdevice (
    id integer NOT NULL,
    name character varying(255),
    active boolean NOT NULL,
    date_created timestamp with time zone,
    device_id uuid,
    registration_id character varying(64) NOT NULL,
    user_id integer
);


ALTER TABLE public.push_notifications_apnsdevice OWNER TO compraloahi;

--
-- Name: push_notifications_apnsdevice_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE push_notifications_apnsdevice_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.push_notifications_apnsdevice_id_seq OWNER TO compraloahi;

--
-- Name: push_notifications_apnsdevice_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE push_notifications_apnsdevice_id_seq OWNED BY push_notifications_apnsdevice.id;


--
-- Name: push_notifications_gcmdevice; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE push_notifications_gcmdevice (
    id integer NOT NULL,
    name character varying(255),
    active boolean NOT NULL,
    date_created timestamp with time zone,
    device_id bigint,
    registration_id text NOT NULL,
    user_id integer
);


ALTER TABLE public.push_notifications_gcmdevice OWNER TO compraloahi;

--
-- Name: push_notifications_gcmdevice_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE push_notifications_gcmdevice_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.push_notifications_gcmdevice_id_seq OWNER TO compraloahi;

--
-- Name: push_notifications_gcmdevice_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE push_notifications_gcmdevice_id_seq OWNED BY push_notifications_gcmdevice.id;


--
-- Name: rating_overallrating; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE rating_overallrating (
    id integer NOT NULL,
    rate numeric(6,1),
    user_id integer NOT NULL
);


ALTER TABLE public.rating_overallrating OWNER TO compraloahi;

--
-- Name: rating_overallrating_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE rating_overallrating_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.rating_overallrating_id_seq OWNER TO compraloahi;

--
-- Name: rating_overallrating_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE rating_overallrating_id_seq OWNED BY rating_overallrating.id;


--
-- Name: rating_rating; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE rating_rating (
    id integer NOT NULL,
    transaction_id integer NOT NULL,
    state integer NOT NULL,
    rate integer,
    created timestamp with time zone NOT NULL,
    transaction_type_id integer NOT NULL,
    voted_id integer NOT NULL,
    voter_id integer NOT NULL,
    CONSTRAINT rating_rating_rate_check CHECK ((rate >= 0)),
    CONSTRAINT rating_rating_transaction_id_check CHECK ((transaction_id >= 0))
);


ALTER TABLE public.rating_rating OWNER TO compraloahi;

--
-- Name: rating_rating_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE rating_rating_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.rating_rating_id_seq OWNER TO compraloahi;

--
-- Name: rating_rating_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE rating_rating_id_seq OWNED BY rating_rating.id;


--
-- Name: report_error_errorreport; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE report_error_errorreport (
    id integer NOT NULL,
    description text NOT NULL,
    date timestamp with time zone NOT NULL,
    screenshot character varying(100)
);


ALTER TABLE public.report_error_errorreport OWNER TO compraloahi;

--
-- Name: report_error_errorreport_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE report_error_errorreport_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.report_error_errorreport_id_seq OWNER TO compraloahi;

--
-- Name: report_error_errorreport_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE report_error_errorreport_id_seq OWNED BY report_error_errorreport.id;


--
-- Name: socialaccount_socialaccount; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE socialaccount_socialaccount (
    id integer NOT NULL,
    provider character varying(30) NOT NULL,
    uid character varying(255) NOT NULL,
    last_login timestamp with time zone NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    extra_data text NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.socialaccount_socialaccount OWNER TO compraloahi;

--
-- Name: socialaccount_socialaccount_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE socialaccount_socialaccount_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.socialaccount_socialaccount_id_seq OWNER TO compraloahi;

--
-- Name: socialaccount_socialaccount_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE socialaccount_socialaccount_id_seq OWNED BY socialaccount_socialaccount.id;


--
-- Name: socialaccount_socialapp; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE socialaccount_socialapp (
    id integer NOT NULL,
    provider character varying(30) NOT NULL,
    name character varying(40) NOT NULL,
    client_id character varying(100) NOT NULL,
    secret character varying(100) NOT NULL,
    key character varying(100) NOT NULL
);


ALTER TABLE public.socialaccount_socialapp OWNER TO compraloahi;

--
-- Name: socialaccount_socialapp_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE socialaccount_socialapp_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.socialaccount_socialapp_id_seq OWNER TO compraloahi;

--
-- Name: socialaccount_socialapp_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE socialaccount_socialapp_id_seq OWNED BY socialaccount_socialapp.id;


--
-- Name: socialaccount_socialapp_sites; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE socialaccount_socialapp_sites (
    id integer NOT NULL,
    socialapp_id integer NOT NULL,
    site_id integer NOT NULL
);


ALTER TABLE public.socialaccount_socialapp_sites OWNER TO compraloahi;

--
-- Name: socialaccount_socialapp_sites_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE socialaccount_socialapp_sites_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.socialaccount_socialapp_sites_id_seq OWNER TO compraloahi;

--
-- Name: socialaccount_socialapp_sites_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE socialaccount_socialapp_sites_id_seq OWNED BY socialaccount_socialapp_sites.id;


--
-- Name: socialaccount_socialtoken; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE socialaccount_socialtoken (
    id integer NOT NULL,
    token text NOT NULL,
    token_secret text NOT NULL,
    expires_at timestamp with time zone,
    account_id integer NOT NULL,
    app_id integer NOT NULL
);


ALTER TABLE public.socialaccount_socialtoken OWNER TO compraloahi;

--
-- Name: socialaccount_socialtoken_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE socialaccount_socialtoken_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.socialaccount_socialtoken_id_seq OWNER TO compraloahi;

--
-- Name: socialaccount_socialtoken_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE socialaccount_socialtoken_id_seq OWNED BY socialaccount_socialtoken.id;


--
-- Name: taggit_tag; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE taggit_tag (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    slug character varying(100) NOT NULL
);


ALTER TABLE public.taggit_tag OWNER TO compraloahi;

--
-- Name: taggit_tag_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE taggit_tag_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.taggit_tag_id_seq OWNER TO compraloahi;

--
-- Name: taggit_tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE taggit_tag_id_seq OWNED BY taggit_tag.id;


--
-- Name: taggit_taggeditem; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE taggit_taggeditem (
    id integer NOT NULL,
    object_id integer NOT NULL,
    content_type_id integer NOT NULL,
    tag_id integer NOT NULL
);


ALTER TABLE public.taggit_taggeditem OWNER TO compraloahi;

--
-- Name: taggit_taggeditem_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE taggit_taggeditem_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.taggit_taggeditem_id_seq OWNER TO compraloahi;

--
-- Name: taggit_taggeditem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE taggit_taggeditem_id_seq OWNED BY taggit_taggeditem.id;


--
-- Name: thumbnail_kvstore; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE thumbnail_kvstore (
    key character varying(200) NOT NULL,
    value text NOT NULL
);


ALTER TABLE public.thumbnail_kvstore OWNER TO compraloahi;

--
-- Name: userProfile_phone; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE "userProfile_phone" (
    id integer NOT NULL,
    number bigint NOT NULL,
    type character varying(200) NOT NULL,
    "userProfile_id" integer NOT NULL
);


ALTER TABLE public."userProfile_phone" OWNER TO compraloahi;

--
-- Name: userProfile_phone_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE "userProfile_phone_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."userProfile_phone_id_seq" OWNER TO compraloahi;

--
-- Name: userProfile_phone_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE "userProfile_phone_id_seq" OWNED BY "userProfile_phone".id;


--
-- Name: userProfile_store; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE "userProfile_store" (
    slug character varying(50) NOT NULL,
    id integer NOT NULL,
    logo character varying(100) NOT NULL,
    name character varying(255) NOT NULL,
    slogan text NOT NULL,
    style json NOT NULL,
    status integer NOT NULL,
    profile_id integer NOT NULL
);


ALTER TABLE public."userProfile_store" OWNER TO compraloahi;

--
-- Name: userProfile_store_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE "userProfile_store_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."userProfile_store_id_seq" OWNER TO compraloahi;

--
-- Name: userProfile_store_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE "userProfile_store_id_seq" OWNED BY "userProfile_store".id;


--
-- Name: userProfile_userlocation; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE "userProfile_userlocation" (
    id integer NOT NULL,
    title character varying(100) NOT NULL,
    lat double precision NOT NULL,
    lng double precision NOT NULL,
    radius integer NOT NULL,
    is_address boolean NOT NULL,
    address json NOT NULL,
    "userProfile_id" integer NOT NULL
);


ALTER TABLE public."userProfile_userlocation" OWNER TO compraloahi;

--
-- Name: userProfile_userlocation_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE "userProfile_userlocation_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."userProfile_userlocation_id_seq" OWNER TO compraloahi;

--
-- Name: userProfile_userlocation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE "userProfile_userlocation_id_seq" OWNED BY "userProfile_userlocation".id;


--
-- Name: userProfile_userprofile; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE "userProfile_userprofile" (
    id integer NOT NULL,
    image character varying(100) NOT NULL,
    birth_date date,
    privacy_settings json NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public."userProfile_userprofile" OWNER TO compraloahi;

--
-- Name: userProfile_userprofile_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE "userProfile_userprofile_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."userProfile_userprofile_id_seq" OWNER TO compraloahi;

--
-- Name: userProfile_userprofile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE "userProfile_userprofile_id_seq" OWNED BY "userProfile_userprofile".id;


--
-- Name: util_counterwhered; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE util_counterwhered (
    id integer NOT NULL,
    whered character varying(100) NOT NULL,
    counter integer NOT NULL
);


ALTER TABLE public.util_counterwhered OWNER TO compraloahi;

--
-- Name: util_counterwhered_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE util_counterwhered_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.util_counterwhered_id_seq OWNER TO compraloahi;

--
-- Name: util_counterwhered_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE util_counterwhered_id_seq OWNED BY util_counterwhered.id;


--
-- Name: util_interested; Type: TABLE; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE TABLE util_interested (
    id integer NOT NULL,
    email character varying(254) NOT NULL,
    seller boolean NOT NULL,
    buyer boolean NOT NULL,
    android boolean NOT NULL,
    ios boolean NOT NULL
);


ALTER TABLE public.util_interested OWNER TO compraloahi;

--
-- Name: util_interested_id_seq; Type: SEQUENCE; Schema: public; Owner: compraloahi
--

CREATE SEQUENCE util_interested_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.util_interested_id_seq OWNER TO compraloahi;

--
-- Name: util_interested_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: compraloahi
--

ALTER SEQUENCE util_interested_id_seq OWNED BY util_interested.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY account_emailaddress ALTER COLUMN id SET DEFAULT nextval('account_emailaddress_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY account_emailconfirmation ALTER COLUMN id SET DEFAULT nextval('account_emailconfirmation_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY "adLocation_adlocation" ALTER COLUMN id SET DEFAULT nextval('"adLocation_adlocation_id_seq"'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY ad_ad ALTER COLUMN id SET DEFAULT nextval('ad_ad_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY ad_ad_categories ALTER COLUMN id SET DEFAULT nextval('ad_ad_categories_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY ad_adimage ALTER COLUMN id SET DEFAULT nextval('ad_adimage_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY ad_category ALTER COLUMN id SET DEFAULT nextval('ad_category_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY corsheaders_corsmodel ALTER COLUMN id SET DEFAULT nextval('corsheaders_corsmodel_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY django_comment_flags ALTER COLUMN id SET DEFAULT nextval('django_comment_flags_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY django_comments ALTER COLUMN id SET DEFAULT nextval('django_comments_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY django_site ALTER COLUMN id SET DEFAULT nextval('django_site_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY faq_question ALTER COLUMN id SET DEFAULT nextval('faq_question_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY faq_questionscore ALTER COLUMN id SET DEFAULT nextval('faq_questionscore_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY faq_topic ALTER COLUMN id SET DEFAULT nextval('faq_topic_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY favorite_favorite ALTER COLUMN id SET DEFAULT nextval('favorite_favorite_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY msg_msg ALTER COLUMN id SET DEFAULT nextval('msg_msg_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY notification_confignotification ALTER COLUMN id SET DEFAULT nextval('notification_confignotification_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY notification_notification ALTER COLUMN id SET DEFAULT nextval('notification_notification_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY push_notifications_apnsdevice ALTER COLUMN id SET DEFAULT nextval('push_notifications_apnsdevice_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY push_notifications_gcmdevice ALTER COLUMN id SET DEFAULT nextval('push_notifications_gcmdevice_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY rating_overallrating ALTER COLUMN id SET DEFAULT nextval('rating_overallrating_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY rating_rating ALTER COLUMN id SET DEFAULT nextval('rating_rating_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY report_error_errorreport ALTER COLUMN id SET DEFAULT nextval('report_error_errorreport_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY socialaccount_socialaccount ALTER COLUMN id SET DEFAULT nextval('socialaccount_socialaccount_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY socialaccount_socialapp ALTER COLUMN id SET DEFAULT nextval('socialaccount_socialapp_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY socialaccount_socialapp_sites ALTER COLUMN id SET DEFAULT nextval('socialaccount_socialapp_sites_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY socialaccount_socialtoken ALTER COLUMN id SET DEFAULT nextval('socialaccount_socialtoken_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY taggit_tag ALTER COLUMN id SET DEFAULT nextval('taggit_tag_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY taggit_taggeditem ALTER COLUMN id SET DEFAULT nextval('taggit_taggeditem_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY "userProfile_phone" ALTER COLUMN id SET DEFAULT nextval('"userProfile_phone_id_seq"'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY "userProfile_store" ALTER COLUMN id SET DEFAULT nextval('"userProfile_store_id_seq"'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY "userProfile_userlocation" ALTER COLUMN id SET DEFAULT nextval('"userProfile_userlocation_id_seq"'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY "userProfile_userprofile" ALTER COLUMN id SET DEFAULT nextval('"userProfile_userprofile_id_seq"'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY util_counterwhered ALTER COLUMN id SET DEFAULT nextval('util_counterwhered_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY util_interested ALTER COLUMN id SET DEFAULT nextval('util_interested_id_seq'::regclass);


--
-- Data for Name: account_emailaddress; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY account_emailaddress (id, email, verified, "primary", user_id) FROM stdin;
1	marianomiles@gmail.com	f	t	2
2	dayhanabelenquiroga@gmail.com	t	t	3
3	mj1182@hotmail.com	f	t	4
\.


--
-- Name: account_emailaddress_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('account_emailaddress_id_seq', 3, true);


--
-- Data for Name: account_emailconfirmation; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY account_emailconfirmation (id, created, sent, key, email_address_id) FROM stdin;
1	2015-12-01 08:52:07.652149-05	2015-12-01 08:52:07.823708-05	sg6ejhqkbpz0tm6tawqonyvleeaa0elcjytkkiukyd5snwfmuboduowmjdk1lf3n	1
2	2015-12-01 10:22:06.191221-05	2015-12-01 10:22:06.211324-05	e4sy6cosd75cwtf1ikjt7z39tti50feodllmgslvfccdzpwne9c1l1gek03baxtm	2
\.


--
-- Name: account_emailconfirmation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('account_emailconfirmation_id_seq', 2, true);


--
-- Data for Name: adLocation_adlocation; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY "adLocation_adlocation" (id, title, lat, lng, address, ad_id) FROM stdin;
1		-13.3027200000000008	-87.1441070000000053	{"administrative_area_level_2": "", "locality": "", "country": "", "lat": "", "administrative_area_level_1": "", "address": "", "lng": "", "nro": ""}	1
2		-31.4183008000000008	-64.1891715000000005	{"administrative_area_level_2": "", "locality": "", "country": "", "lat": "", "administrative_area_level_1": "", "address": "", "lng": "", "nro": ""}	2
3		-31.4183008000000008	-64.1891715000000005	{"administrative_area_level_2": "", "locality": "", "country": "", "lat": "", "administrative_area_level_1": "", "address": "", "lng": "", "nro": ""}	3
4		-31.4183008000000008	-64.1891715000000005	{"administrative_area_level_2": "", "locality": "", "country": "", "lat": "", "administrative_area_level_1": "", "address": "", "lng": "", "nro": ""}	4
\.


--
-- Name: adLocation_adlocation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('"adLocation_adlocation_id_seq"', 4, true);


--
-- Data for Name: ad_ad; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY ad_ad (id, title, body, created, modified, pub_date, slug, published, status, short_description, price, store_published, author_id) FROM stdin;
1	Equipo de GNC 5ta Generación	<p style="margin-bottom: 1.5em; padding: 0px; border: 0px; font-stretch: inherit; line-height: 18px; font-family: Helvetica, Arial, sans-serif; font-size: 12px; vertical-align: baseline; color: rgb(51, 51, 51); background-color: rgba(255, 255, 255, 0.8);">:: AHORR&Aacute; CON GNC :: Promoci&oacute;n Especial</p>\n\n<p style="margin-bottom: 1.5em; padding: 0px; border: 0px; font-stretch: inherit; line-height: 18px; font-family: Helvetica, Arial, sans-serif; font-size: 12px; vertical-align: baseline; color: rgb(51, 51, 51); background-color: rgba(255, 255, 255, 0.8);">Instal&aacute; tu Equipo de GNC 5ta Generaci&oacute;n + Tubo 10 mts + Carga Externa + Oblea + Instalaci&oacute;n Completa + Garant&iacute;a Escrita por 1 a&ntilde;o por $ 12.500 INSTALAMOS EN EL D&Iacute;A &gt;&gt; Aprovechalo ahora! Hac&eacute; tu Consulta &lt;&lt;</p>\n\n<p style="margin-bottom: 1.5em; padding: 0px; border: 0px; font-stretch: inherit; line-height: 18px; font-family: Helvetica, Arial, sans-serif; font-size: 12px; vertical-align: baseline; color: rgb(51, 51, 51); background-color: rgba(255, 255, 255, 0.8);">Ahorra con GNC! Cotiz&aacute; tu equipo Comunicate con nosotros al (0351) 438-5556 o visitanos en Mendoza 2980 (Alta C&oacute;rdoba) y coordinamos la mejor manera de que vos puedas tener tu equipo de GNC.</p>\n\n<p style="margin-bottom: 1.5em; padding: 0px; border: 0px; font-stretch: inherit; line-height: 18px; font-family: Helvetica, Arial, sans-serif; font-size: 12px; vertical-align: baseline; color: rgb(51, 51, 51); background-color: rgba(255, 255, 255, 0.8);">www.fortezzagas.com</p>	2015-12-01 08:58:06.272056-05	2015-12-01 08:58:06.272111-05	2015-12-01 08:58:06.272141-05	equipo-de-gnc-5ta-generacion	t	1	Equipo de GNC 5ta Generación con tubo de 10 mts, oblea, instalación y carga externa	12500.00	f	2
2	Pinza Amperometrica	<h2 dir="ltr" id="docs-internal-guid-51619ad6-5e25-feff-caab-5237a12b90cb" style="line-height: 1.38; margin-top: 0pt; margin-bottom: 0pt;"><span style="font-size:14.666666666666666px;font-family:Arial;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Pinza amperom&eacute;trica MARCA KYORITSU Max: 600v &amp; 600a: $500</span></h2>\n\n<h3><strong><span style="font-size:14.666666666666666px;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">&nbsp;- Con estuche de cuero</span></strong></h3>	2015-12-01 10:28:01.326256-05	2015-12-01 10:28:01.326289-05	2015-12-01 10:28:01.326304-05	pinza-amperometrica	t	1	Pinza amperométrica MARCA KYORITSU	600.00	f	3
3	Micrometro 0-25 mm X 0.01 mm	<h1 dir="ltr" id="docs-internal-guid-51619ad6-5e29-c9ea-8f7f-8586acd7e989" style="line-height: 1.38; margin-top: 0pt; margin-bottom: 0pt; text-align: center;"><span style="font-size:14.666666666666666px;font-family:Arial;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Micrometro 0-25 mm X 0.01 mm MARCA SHANGHAI: $400</span></h1>\n\n<p><span style="font-size:14.666666666666666px;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">&nbsp;- Con caja de madera</span></p>	2015-12-01 10:31:52.933216-05	2015-12-01 10:31:52.933249-05	2015-12-01 10:31:52.933263-05	micrometro-0-25-mm-x-001-mm	t	1	Micrometro 0-25 mm X 0.01 mm MARCA SHANGHAI	400.00	f	3
4	Juego de 6 llaves  MARCA BANGO	<p dir="ltr" id="docs-internal-guid-827e5c76-5e79-79eb-db8f-ee652e27abba" style="line-height: 1.38; margin-top: 0pt; margin-bottom: 0pt; text-align: center;"><span style="font-size:14.666666666666666px;font-family:Arial;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Juego de 6 llaves boca/boca MARCA BANGO: $500</span></p>\n\n<p dir="ltr" style="line-height: 1.38; margin-top: 0pt; margin-bottom: 0pt; text-align: center;">&nbsp;</p>\n\n<p dir="ltr" style="line-height: 1.38; margin-top: 0pt; margin-bottom: 0pt; text-align: center;"><span style="font-size:14.666666666666666px;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">&nbsp;1 - Numero 20-20: boca/boca</span></p>\n\n<p dir="ltr" style="line-height: 1.38; margin-top: 0pt; margin-bottom: 0pt; text-align: center;"><span style="font-size:14.666666666666666px;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">&nbsp;2 - Numero 21-23: boca/boca</span></p>\n\n<p dir="ltr" style="line-height: 1.38; margin-top: 0pt; margin-bottom: 0pt; text-align: center;"><span style="font-size:14.666666666666666px;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">&nbsp;3 - Numero 24-27: boca/boca</span></p>\n\n<p dir="ltr" style="line-height: 1.38; margin-top: 0pt; margin-bottom: 0pt; text-align: center;"><span style="font-size:14.666666666666666px;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">&nbsp;4 - Numero 28: boca/estriada</span></p>\n\n<p dir="ltr" style="line-height: 1.38; margin-top: 0pt; margin-bottom: 0pt; text-align: center;"><span style="font-size:14.666666666666666px;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">&nbsp;5 - Numero 30-32: boca/boca</span></p>\n\n<p dir="ltr" style="line-height: 1.38; margin-top: 0pt; margin-bottom: 0pt; text-align: center;"><span style="font-size:14.666666666666666px;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">6- &nbsp;numero 30-32: estriada/estriada</span></p>\n\n<p style="text-align: center;"><br />\n<span style="font-size:14.666666666666666px;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">// EN LAS FOTOS HAY MAS LLAVES QUE EL JUEGO EN VENTA//</span></p>	2015-12-01 12:09:13.1345-05	2015-12-01 12:09:13.134534-05	2015-12-01 12:09:13.134549-05	juego-de-6-llaves-marca-bango	t	1	Juego de 6 llaves boca/boca MARCA BANGO	500.00	f	3
\.


--
-- Data for Name: ad_ad_categories; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY ad_ad_categories (id, ad_id, category_id) FROM stdin;
\.


--
-- Name: ad_ad_categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('ad_ad_categories_id_seq', 1, false);


--
-- Name: ad_ad_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('ad_ad_id_seq', 4, true);


--
-- Data for Name: ad_adimage; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY ad_adimage (id, image, "default", ad_id_id) FROM stdin;
1	ad/gnc1.jpg	t	1
2	ad/GEDC1938.JPG	t	2
3	ad/GEDC1939.JPG	f	2
4	ad/GEDC1940.JPG	f	2
5	ad/GEDC1935.JPG	f	3
6	ad/GEDC1936.JPG	t	3
7	ad/GEDC1937.JPG	f	3
8	ad/GEDC1941.JPG	t	4
9	ad/GEDC1942.JPG	f	4
10	ad/GEDC1943.JPG	f	4
11	ad/GEDC1945.JPG	f	4
\.


--
-- Name: ad_adimage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('ad_adimage_id_seq', 11, true);


--
-- Data for Name: ad_category; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY ad_category (id, name, slug) FROM stdin;
1	Otras categorias	otras-categorias
2	Juegos y Jugetes	juegos-y-jugetes
3	Industria	industria
4	Oficina	oficina
5	Electronica	electronica
6	Bebes	bebes
7	Antiguedades	antiguedades
8	Accesorio para vehiculos	accesorio-para-vehiculos
9	Musica, Peliculas y Series	musica-peliculas-y-series
10	Electrodomesticos	electrodomesticos
11	Casa	casa
12	Deportes	deportes
13	Herramientas	herramientas
14	Salud	salud
15	Intrumentos musicales	intrumentos-musicales
16	Belleza	belleza
17	Servicio	servicio
18	Inmuebles	inmuebles
19	Tecnologia	tecnologia
20	Autos	autos
21	Muebles	muebles
22	Bazar	bazar
23	Indumentaria	indumentaria
\.


--
-- Name: ad_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('ad_category_id_seq', 23, true);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add permission	2	add_permission
5	Can change permission	2	change_permission
6	Can delete permission	2	delete_permission
7	Can add group	3	add_group
8	Can change group	3	change_group
9	Can delete group	3	delete_group
10	Can add user	4	add_user
11	Can change user	4	change_user
12	Can delete user	4	delete_user
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add site	7	add_site
20	Can change site	7	change_site
21	Can delete site	7	delete_site
22	Can add email address	8	add_emailaddress
23	Can change email address	8	change_emailaddress
24	Can delete email address	8	delete_emailaddress
25	Can add email confirmation	9	add_emailconfirmation
26	Can change email confirmation	9	change_emailconfirmation
27	Can delete email confirmation	9	delete_emailconfirmation
28	Can add social application	10	add_socialapp
29	Can change social application	10	change_socialapp
30	Can delete social application	10	delete_socialapp
31	Can add social account	11	add_socialaccount
32	Can change social account	11	change_socialaccount
33	Can delete social account	11	delete_socialaccount
34	Can add social application token	12	add_socialtoken
35	Can change social application token	12	change_socialtoken
36	Can delete social application token	12	delete_socialtoken
37	Can add Tag	13	add_tag
38	Can change Tag	13	change_tag
39	Can delete Tag	13	delete_tag
40	Can add Tagged Item	14	add_taggeditem
41	Can change Tagged Item	14	change_taggeditem
42	Can delete Tagged Item	14	delete_taggeditem
43	Can add kv store	15	add_kvstore
44	Can change kv store	15	change_kvstore
45	Can delete kv store	15	delete_kvstore
46	Can add comment	16	add_comment
47	Can change comment	16	change_comment
48	Can delete comment	16	delete_comment
49	Can moderate comments	16	can_moderate
50	Can add comment flag	17	add_commentflag
51	Can change comment flag	17	change_commentflag
52	Can delete comment flag	17	delete_commentflag
53	Can add xtd comment	18	add_xtdcomment
54	Can change xtd comment	18	change_xtdcomment
55	Can delete xtd comment	18	delete_xtdcomment
56	Can add cors model	19	add_corsmodel
57	Can change cors model	19	change_corsmodel
58	Can delete cors model	19	delete_corsmodel
59	Can add token	20	add_token
60	Can change token	20	change_token
61	Can delete token	20	delete_token
62	Can add GCM device	21	add_gcmdevice
63	Can change GCM device	21	change_gcmdevice
64	Can delete GCM device	21	delete_gcmdevice
65	Can add APNS device	22	add_apnsdevice
66	Can change APNS device	22	change_apnsdevice
67	Can delete APNS device	22	delete_apnsdevice
68	Can add Message	23	add_message
69	Can change Message	23	change_message
70	Can delete Message	23	delete_message
71	Can add category	24	add_category
72	Can change category	24	change_category
73	Can delete category	24	delete_category
74	Can add Ad	25	add_ad
75	Can change Ad	25	change_ad
76	Can delete Ad	25	delete_ad
77	Can add ad image	26	add_adimage
78	Can change ad image	26	change_adimage
79	Can delete ad image	26	delete_adimage
80	Can add ad location	27	add_adlocation
81	Can change ad location	27	change_adlocation
82	Can delete ad location	27	delete_adlocation
83	Can add user profile	28	add_userprofile
84	Can change user profile	28	change_userprofile
85	Can delete user profile	28	delete_userprofile
86	Can add phone	29	add_phone
87	Can change phone	29	change_phone
88	Can delete phone	29	delete_phone
89	Can add user location	30	add_userlocation
90	Can change user location	30	change_userlocation
91	Can delete user location	30	delete_userlocation
92	Can add store	31	add_store
93	Can change store	31	change_store
94	Can delete store	31	delete_store
95	Can add config notification	32	add_confignotification
96	Can change config notification	32	change_confignotification
97	Can delete config notification	32	delete_confignotification
98	Can add Notification	33	add_notification
99	Can change Notification	33	change_notification
100	Can delete Notification	33	delete_notification
101	Can add overall rating	34	add_overallrating
102	Can change overall rating	34	change_overallrating
103	Can delete overall rating	34	delete_overallrating
104	Can add rating	35	add_rating
105	Can change rating	35	change_rating
106	Can delete rating	35	delete_rating
107	Can add message	36	add_msg
108	Can change message	36	change_msg
109	Can delete message	36	delete_msg
110	Can add favorite	37	add_favorite
111	Can change favorite	37	change_favorite
112	Can delete favorite	37	delete_favorite
113	Can add Topic	38	add_topic
114	Can change Topic	38	change_topic
115	Can delete Topic	38	delete_topic
116	Can add Frequent asked question	39	add_question
117	Can change Frequent asked question	39	change_question
118	Can delete Frequent asked question	39	delete_question
119	Can add question score	40	add_questionscore
120	Can change question score	40	change_questionscore
121	Can delete question score	40	delete_questionscore
122	Can add error report	41	add_errorreport
123	Can change error report	41	change_errorreport
124	Can delete error report	41	delete_errorreport
125	Can add interested	42	add_interested
126	Can change interested	42	change_interested
127	Can delete interested	42	delete_interested
128	Can add counter whered	43	add_counterwhered
129	Can change counter whered	43	change_counterwhered
130	Can delete counter whered	43	delete_counterwhered
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('auth_permission_id_seq', 130, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
2	pbkdf2_sha256$20000$ppRZdzddnTpB$CqoKSFUC0YubxeLituMu4CBj6wfFC40RHH2FFRt0XPQ=	2015-12-01 08:52:07.846335-05	f	marianomiles			marianomiles@gmail.com	f	t	2015-12-01 08:52:07.587665-05
1	pbkdf2_sha256$20000$uJH3vGk4MZNn$+UAjXP8g3wuHXTnAespZlXW8D4I24fK5mW0wwdXQLtM=	2015-12-01 08:54:45.983312-05	t	nuestroadmin			contextinformatic@gmail.com	t	t	2015-11-30 22:51:14.510588-05
3	pbkdf2_sha256$20000$B9CNEMy9Dcs9$LBTEOjIeTl5q9rzanCKVLV/HeOlI5lsSJfGxkNZk3/8=	2015-12-01 11:53:46.251115-05	f	dbq			dayhanabelenquiroga@gmail.com	f	t	2015-12-01 10:22:06.148336-05
4	!y1cjeMISAZygSu6XTTSnOYfEXBesH8GE7UgRPzQ6	2015-12-01 12:29:16.250117-05	f	marcos	Marcos	Barroso	mj1182@hotmail.com	f	t	2015-12-01 12:29:16.17797-05
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('auth_user_id_seq', 4, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: authtoken_token; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY authtoken_token (key, created, user_id) FROM stdin;
\.


--
-- Data for Name: corsheaders_corsmodel; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY corsheaders_corsmodel (id, cors) FROM stdin;
\.


--
-- Name: corsheaders_corsmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('corsheaders_corsmodel_id_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2015-11-30 22:54:15.703215-05	1	compraloahi.com.ar	2	Modificado/a domain y name.	7	1
2	2015-11-30 22:54:55.751599-05	1	Facebook App	1		10	1
3	2015-11-30 22:55:17.933986-05	2	Google App	1		10	1
4	2015-11-30 22:55:58.257472-05	1	Otras categorias	1		24	1
5	2015-11-30 22:56:07.578611-05	2	Juegos y Jugetes	1		24	1
6	2015-11-30 22:56:13.880397-05	3	Industria	1		24	1
7	2015-11-30 22:56:19.083795-05	4	Oficina	1		24	1
8	2015-11-30 22:56:24.840325-05	5	Electronica	1		24	1
9	2015-11-30 22:56:29.945362-05	6	Bebes	1		24	1
10	2015-11-30 22:56:34.665653-05	7	Antiguedades	1		24	1
11	2015-11-30 22:56:40.83734-05	8	Accesorio para vehiculos	1		24	1
12	2015-11-30 22:56:46.443433-05	9	Musica, Peliculas y Series	1		24	1
13	2015-11-30 22:56:51.912639-05	10	Electrodomesticos	1		24	1
14	2015-11-30 22:56:56.537456-05	11	Casa	1		24	1
15	2015-11-30 22:57:02.60656-05	12	Deportes	1		24	1
16	2015-11-30 22:57:10.98271-05	13	Herramientas	1		24	1
17	2015-11-30 22:57:18.776619-05	14	Salud	1		24	1
18	2015-11-30 22:57:27.886128-05	15	Intrumentos musicales	1		24	1
19	2015-11-30 22:57:33.357852-05	16	Belleza	1		24	1
20	2015-11-30 22:57:38.883706-05	17	Servicio	1		24	1
21	2015-11-30 22:57:45.595496-05	18	Inmuebles	1		24	1
22	2015-11-30 22:57:54.751429-05	19	Tecnologia	1		24	1
23	2015-11-30 22:58:00.089966-05	20	Autos	1		24	1
24	2015-11-30 22:58:04.949338-05	21	Muebles	1		24	1
25	2015-11-30 22:58:09.654966-05	22	Bazar	1		24	1
26	2015-11-30 22:58:15.293381-05	23	Indumentaria	1		24	1
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 26, true);


--
-- Data for Name: django_comment_flags; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY django_comment_flags (id, flag, flag_date, comment_id, user_id) FROM stdin;
\.


--
-- Name: django_comment_flags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('django_comment_flags_id_seq', 1, false);


--
-- Data for Name: django_comments; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY django_comments (id, object_pk, user_name, user_email, user_url, comment, submit_date, ip_address, is_public, is_removed, content_type_id, site_id, user_id) FROM stdin;
\.


--
-- Name: django_comments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('django_comments_id_seq', 1, false);


--
-- Data for Name: django_comments_xtd_xtdcomment; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY django_comments_xtd_xtdcomment (comment_ptr_id, thread_id, parent_id, level, "order", followup) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	sites	site
8	account	emailaddress
9	account	emailconfirmation
10	socialaccount	socialapp
11	socialaccount	socialaccount
12	socialaccount	socialtoken
13	taggit	tag
14	taggit	taggeditem
15	thumbnail	kvstore
16	django_comments	comment
17	django_comments	commentflag
18	django_comments_xtd	xtdcomment
19	corsheaders	corsmodel
20	authtoken	token
21	push_notifications	gcmdevice
22	push_notifications	apnsdevice
23	djmail	message
24	ad	category
25	ad	ad
26	ad	adimage
27	adLocation	adlocation
28	userProfile	userprofile
29	userProfile	phone
30	userProfile	userlocation
31	userProfile	store
32	notification	confignotification
33	notification	notification
34	rating	overallrating
35	rating	rating
36	msg	msg
37	favorite	favorite
38	faq	topic
39	faq	question
40	faq	questionscore
41	report_error	errorreport
42	util	interested
43	util	counterwhered
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('django_content_type_id_seq', 43, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2015-11-30 22:49:39.119037-05
2	auth	0001_initial	2015-11-30 22:49:39.212941-05
3	account	0001_initial	2015-11-30 22:49:39.278193-05
4	account	0002_email_max_length	2015-11-30 22:49:39.304132-05
5	taggit	0001_initial	2015-11-30 22:49:39.403058-05
6	ad	0001_initial	2015-11-30 22:49:39.586575-05
7	adLocation	0001_initial	2015-11-30 22:49:39.634716-05
8	admin	0001_initial	2015-11-30 22:49:39.691207-05
9	contenttypes	0002_remove_content_type_name	2015-11-30 22:49:39.857758-05
10	auth	0002_alter_permission_name_max_length	2015-11-30 22:49:39.898882-05
11	auth	0003_alter_user_email_max_length	2015-11-30 22:49:39.943275-05
12	auth	0004_alter_user_username_opts	2015-11-30 22:49:39.982826-05
13	auth	0005_alter_user_last_login_null	2015-11-30 22:49:40.02664-05
14	auth	0006_require_contenttypes_0002	2015-11-30 22:49:40.02931-05
15	authtoken	0001_initial	2015-11-30 22:49:40.088304-05
16	sites	0001_initial	2015-11-30 22:49:40.111086-05
17	django_comments	0001_initial	2015-11-30 22:49:40.309591-05
18	django_comments	0002_update_user_email_field_length	2015-11-30 22:49:40.367172-05
19	django_comments_xtd	0001_initial	2015-11-30 22:49:40.436939-05
20	djmail	0001_initial	2015-11-30 22:49:40.45892-05
21	faq	0001_initial	2015-11-30 22:49:40.8303-05
22	favorite	0001_initial	2015-11-30 22:49:41.170216-05
23	msg	0001_initial	2015-11-30 22:49:41.262733-05
24	notification	0001_initial	2015-11-30 22:49:41.422303-05
25	push_notifications	0001_initial	2015-11-30 22:49:41.602946-05
26	push_notifications	0002_auto_20150821_0134	2015-11-30 22:49:41.755422-05
27	rating	0001_initial	2015-11-30 22:49:41.987986-05
28	sessions	0001_initial	2015-11-30 22:49:42.037358-05
29	socialaccount	0001_initial	2015-11-30 22:49:42.547923-05
30	userProfile	0001_initial	2015-11-30 22:49:43.219141-05
31	util	0001_initial	2015-11-30 22:49:43.284873-05
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('django_migrations_id_seq', 31, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
detp397rzazu8cwa3v156hbrm26alxol	ZjA0Y2YzODcyZjdmYzE1MWFlYjhlYmZkMDRjMmY0YzUwZDc3N2Y4ODp7InNvY2lhbGFjY291bnRfc3RhdGUiOlt7InNjb3BlIjoiIiwicHJvY2VzcyI6ImxvZ2luIiwiYXV0aF9wYXJhbXMiOiIifSwiNFpnNXNDNm1lc1A2Il19	2015-12-15 01:24:03.706849-05
xa7hhf6mf0bnqhxiknrnd42uls05d3dj	NTUyN2RiMmVkMzg0MzVjNmUxYTQzMzFmNWJkOWM3OGNjNjBhYWM5YTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiYWxsYXV0aC5hY2NvdW50LmF1dGhfYmFja2VuZHMuQXV0aGVudGljYXRpb25CYWNrZW5kIiwiYWNjb3VudF92ZXJpZmllZF9lbWFpbCI6bnVsbCwiYWNjb3VudF91c2VyIjoiMiIsIl9hdXRoX3VzZXJfaGFzaCI6ImU0NzQ1NTVhYTAxMzg4MzhlYTVhZDZhYWE2ZWYzMDIzNWFhOTU3NjIifQ==	2015-12-15 08:52:07.874289-05
xir9lzch40c71jceacj76oe18dniqim3	MGM2NWM0N2U2YWRmYjAxMjM1NTY3YjA2M2ZjNDY1MDdkOWZmNGM2Mjp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiYWxsYXV0aC5hY2NvdW50LmF1dGhfYmFja2VuZHMuQXV0aGVudGljYXRpb25CYWNrZW5kIiwiYWNjb3VudF92ZXJpZmllZF9lbWFpbCI6bnVsbCwiYWNjb3VudF91c2VyIjoiMyIsIl9hdXRoX3VzZXJfaGFzaCI6Ijc3ZGY5ZTdmZWY0Y2I1ZDViYTNjMTA5N2ExYTIxMjAzYmNhZmRlZjcifQ==	2015-12-15 10:22:06.241733-05
hr0d2bp8nc05xvioquyeg69ez2to0rdg	MTM4NThlNGJkOTEyNzkxYWM1ODgzOTI0YTg0M2Y2MTFkOTUxMDAxMjp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3N2RmOWU3ZmVmNGNiNWQ1YmEzYzEwOTdhMWEyMTIwM2JjYWZkZWY3IiwiX3Nlc3Npb25fZXhwaXJ5IjowfQ==	2015-12-15 11:53:46.254894-05
l0twu7w9ik6az2596rukao67wbyrsi31	MTQxZDI4YWMxNTJjMzEwYjAwMzJjNWRlYWEzMjgyYjQyYzkwZTljYzp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiYWxsYXV0aC5hY2NvdW50LmF1dGhfYmFja2VuZHMuQXV0aGVudGljYXRpb25CYWNrZW5kIiwiYWNjb3VudF92ZXJpZmllZF9lbWFpbCI6bnVsbCwiX2F1dGhfdXNlcl9oYXNoIjoiNDBjMDg1MWU3MDg0ZDllNDRhY2JiZTk5ZmYzMjBlYTU1ODFhNDg2NSJ9	2015-12-15 12:29:16.257486-05
\.


--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY django_site (id, domain, name) FROM stdin;
1	compraloahi.com.ar	compraloahi.com.ar
\.


--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('django_site_id_seq', 1, true);


--
-- Data for Name: djmail_message; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY djmail_message (uuid, from_email, to_email, body_text, body_html, subject, data, retry_count, status, priority, created_at, sent_at, exception) FROM stdin;
b64a8856-9832-11e5-a5f5-0401521cbb01	notificacion@compraloahi.com.ar	marianomiles@gmail.com	El usuario marianomiles de compraloahi.com.ar ha proporcionado este como su correo electrónico.\n\nPara confirmar que esto es correcto, haga clic en https://compraloahi.com.ar/accounts/confirm-email/sg6ejhqkbpz0tm6tawqonyvleeaa0elcjytkkiukyd5snwfmuboduowmjdk1lf3n/		[compraloahi.com.ar] Confirmar dirección de correo electrónico	gANjZGphbmdvLmNvcmUubWFpbC5tZXNzYWdlCkVtYWlsTXVsdGlBbHRlcm5hdGl2ZXMKcQApgXEBfXECKFgEAAAAYm9keXEDWAcBAABFbCB1c3VhcmlvIG1hcmlhbm9taWxlcyBkZSBjb21wcmFsb2FoaS5jb20uYXIgaGEgcHJvcG9yY2lvbmFkbyBlc3RlIGNvbW8gc3UgY29ycmVvIGVsZWN0csOzbmljby4KClBhcmEgY29uZmlybWFyIHF1ZSBlc3RvIGVzIGNvcnJlY3RvLCBoYWdhIGNsaWMgZW4gaHR0cHM6Ly9jb21wcmFsb2FoaS5jb20uYXIvYWNjb3VudHMvY29uZmlybS1lbWFpbC9zZzZlamhxa2JwejB0bTZ0YXdxb255dmxlZWFhMGVsY2p5dGtraXVreWQ1c253Zm11Ym9kdW93bWpkazFsZjNuL3EEWAIAAAB0b3EFXXEGWBYAAABtYXJpYW5vbWlsZXNAZ21haWwuY29tcQdhWAoAAABjb25uZWN0aW9ucQhjZGptYWlsLmJhY2tlbmRzLmFzeW5jCkVtYWlsQmFja2VuZApxCSmBcQp9cQsoWAQAAABhcmdzcQwpWAYAAABrd2FyZ3NxDX1xDlgNAAAAZmFpbF9zaWxlbnRseXEPiXN1YlgHAAAAc3ViamVjdHEQWEAAAABbY29tcHJhbG9haGkuY29tLmFyXSBDb25maXJtYXIgZGlyZWNjacOzbiBkZSBjb3JyZW8gZWxlY3Ryw7NuaWNvcRFYAwAAAGJjY3ESXXETWAwAAABhbHRlcm5hdGl2ZXNxFF1xFVgNAAAAZXh0cmFfaGVhZGVyc3EWfXEXWAsAAABhdHRhY2htZW50c3EYXXEZWAgAAAByZXBseV90b3EaXXEbWAIAAABjY3EcXXEdWAoAAABmcm9tX2VtYWlscR5YHwAAAG5vdGlmaWNhY2lvbkBjb21wcmFsb2FoaS5jb20uYXJxH3ViLg==	-1	30	50	2015-12-01 08:52:07.900954-05	2015-12-01 08:52:09.632945-05	
47f6fb84-983f-11e5-964a-0401521cbb01	notificacion@compraloahi.com.ar	dayhanabelenquiroga@gmail.com	El usuario dbq de compraloahi.com.ar ha proporcionado este como su correo electrónico.\n\nPara confirmar que esto es correcto, haga clic en https://compraloahi.com.ar/accounts/confirm-email/e4sy6cosd75cwtf1ikjt7z39tti50feodllmgslvfccdzpwne9c1l1gek03baxtm/		[compraloahi.com.ar] Confirmar dirección de correo electrónico	gANjZGphbmdvLmNvcmUubWFpbC5tZXNzYWdlCkVtYWlsTXVsdGlBbHRlcm5hdGl2ZXMKcQApgXEBfXECKFgEAAAAYm9keXEDWP4AAABFbCB1c3VhcmlvIGRicSBkZSBjb21wcmFsb2FoaS5jb20uYXIgaGEgcHJvcG9yY2lvbmFkbyBlc3RlIGNvbW8gc3UgY29ycmVvIGVsZWN0csOzbmljby4KClBhcmEgY29uZmlybWFyIHF1ZSBlc3RvIGVzIGNvcnJlY3RvLCBoYWdhIGNsaWMgZW4gaHR0cHM6Ly9jb21wcmFsb2FoaS5jb20uYXIvYWNjb3VudHMvY29uZmlybS1lbWFpbC9lNHN5NmNvc2Q3NWN3dGYxaWtqdDd6Mzl0dGk1MGZlb2RsbG1nc2x2ZmNjZHpwd25lOWMxbDFnZWswM2JheHRtL3EEWAIAAAB0b3EFXXEGWB0AAABkYXloYW5hYmVsZW5xdWlyb2dhQGdtYWlsLmNvbXEHYVgKAAAAY29ubmVjdGlvbnEIY2RqbWFpbC5iYWNrZW5kcy5hc3luYwpFbWFpbEJhY2tlbmQKcQkpgXEKfXELKFgEAAAAYXJnc3EMKVgGAAAAa3dhcmdzcQ19cQ5YDQAAAGZhaWxfc2lsZW50bHlxD4lzdWJYBwAAAHN1YmplY3RxEFhAAAAAW2NvbXByYWxvYWhpLmNvbS5hcl0gQ29uZmlybWFyIGRpcmVjY2nDs24gZGUgY29ycmVvIGVsZWN0csOzbmljb3ERWAMAAABiY2NxEl1xE1gMAAAAYWx0ZXJuYXRpdmVzcRRdcRVYDQAAAGV4dHJhX2hlYWRlcnNxFn1xF1gLAAAAYXR0YWNobWVudHNxGF1xGVgIAAAAcmVwbHlfdG9xGl1xG1gCAAAAY2NxHF1xHVgKAAAAZnJvbV9lbWFpbHEeWB8AAABub3RpZmljYWNpb25AY29tcHJhbG9haGkuY29tLmFycR91Yi4=	-1	30	50	2015-12-01 10:22:06.26094-05	2015-12-01 10:22:07.801844-05	
\.


--
-- Data for Name: faq_question; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY faq_question (id, text, answer, slug, status, protected, sort_order, created_on, updated_on, nr_views, created_by_id, topic_id, updated_by_id) FROM stdin;
1	¿Tiene algun costo Compraloahi?	No, Compraloahí no tiene ningun costo alguno tanto para realizar busquedas de productos y/o servicios como también para subir anuncios de productos y/o servicios.	tiene-algun-costo-compraloahi	1	f	0	2015-11-30 16:11:26.208-05	2015-11-30 16:17:01.246-05	0	\N	3	\N
2	¿Como subo mis productos?	Subí tus productos creando un aviso ingresando a: Entra>>Panel>>Crear aviso ó Entra>>Panel>>Mis avisos>>Crear aviso\r\nRecordá: Para crear un aviso es necesario estar registrado. 	como-subo-mis-productos	1	f	0	2015-11-30 16:37:57.891-05	2015-11-30 16:51:05.459-05	0	\N	2	\N
3	¿Como se hace una busqueda?	Para realizar busquedas de productos y/o servicios ingresá lo que quieras en la barra de navegación que se encuentra en la parte superior del sitio en el centro, allí podras buscar lo que necesitás y automaticamente te muestra los productos o servicios que se encuentran cerca de la ubicación en la que te encuentres.\r\n\r\nRecordá: Podes modificar la ubicación en la cual queres hacer tu busqueda, por medio de:\r\nBuscar(en la barra superior)>>Ingresar una ubicación(a la izquierda del mapa).\r\n\r\nRecordá: Es necesario permitir a nuestro navegador compartir nuestra ubicación para que el servicio pueda funcionar. 	como-se-hace-una-busqueda	1	f	0	2015-11-30 16:50:48.579-05	2015-11-30 16:51:05.469-05	0	\N	1	\N
4	¿Puedo crear un aviso sin tener un comercio?	Si, cualquier persona que tenga para ofrecer un producto o servicio puede crear un aviso, solo hay que tener en cuenta que es necesario el ingreso de una ubicación de este producto o servicio para que luego quien realice una busqueda con esas caractrísticas lo pueda encontrar de acuerdo a su proximidad.	puedo-crear-un-aviso-sin-tener-un-comercio	1	f	0	2015-11-30 17:05:12.472-05	2015-11-30 17:12:53.086-05	0	\N	2	\N
5	¿Como funciona Compraloahí?	Compraloahí funciona de manera muy simple: una persona (comprador) realiza una búsqueda de un producto o servicio de su interés, donde otra persona (vendedor) publicó anteriormente lo que ofrece. Esta busqueda que hace el comprador filtra los avisos de vendedores de acuerdo a su proximidad, es decir, que solo los productos y servicios que estarán cerca del comprador seran mostrados y así, poder ver información relevante para luego acercarse a la ubicación que el vendedor especificó, ir y realizar la adquisicion de este producto o servicio personalmente. 	como-funciona-compraloahi	1	f	0	2015-11-30 17:12:37.62-05	2015-11-30 17:12:53.094-05	0	\N	3	\N
\.


--
-- Name: faq_question_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('faq_question_id_seq', 5, true);


--
-- Data for Name: faq_questionscore; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY faq_questionscore (id, score, ip_address, question_id, user_id) FROM stdin;
1	1	181.164.151.84	1	1
2	1	181.164.151.84	1	\N
3	1	66.249.64.55	5	\N
4	1	66.249.64.55	2	\N
5	0	66.249.64.55	4	\N
6	0	66.249.64.55	1	\N
7	0	66.249.64.55	3	\N
8	1	190.245.195.170	3	\N
\.


--
-- Name: faq_questionscore_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('faq_questionscore_id_seq', 8, true);


--
-- Data for Name: faq_topic; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY faq_topic (id, name, slug, sort_order, nr_views, icon, created_on, updated_on, description, created_by_id, site_id, updated_by_id) FROM stdin;
3	Preguntas generales	preguntas-generales	0	11		2015-11-30 16:05:03.217-05	2015-12-01 06:34:34.661544-05	Preguntas generales del sitio.	\N	1	\N
1	Buscar un anuncio	buscar-un-anuncio	0	5		2015-11-30 14:37:18.103-05	2015-12-01 06:34:42.274247-05	Preguntas frecuentes relaciadas a buscar un producto o servicio	\N	1	\N
2	Crear un anuncio	crear-un-anuncio	0	3		2015-11-30 14:37:52.302-05	2015-12-01 06:34:42.910154-05	Preguntas frecuentes relaciadas a crear un producto o servicio	\N	1	\N
\.


--
-- Name: faq_topic_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('faq_topic_id_seq', 3, true);


--
-- Data for Name: favorite_favorite; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY favorite_favorite (id, target_object_id, "timestamp", target_content_type_id, user_id) FROM stdin;
\.


--
-- Name: favorite_favorite_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('favorite_favorite_id_seq', 3, true);


--
-- Data for Name: msg_msg; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY msg_msg (id, subject, body, sent_at, read_at, replied_at, sender_archived, recipient_archived, sender_deleted_at, recipient_deleted_at, moderation_status, moderation_date, moderation_reason, object_id, content_type_id, parent_id, recipient_id, sender_id, thread_id) FROM stdin;
\.


--
-- Name: msg_msg_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('msg_msg_id_seq', 1, false);


--
-- Data for Name: notification_confignotification; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY notification_confignotification (id, config, user_id) FROM stdin;
1	{"cmmt": {"email": true, "label": "Desea recibir una notificacion cuando commentan un aviso propio", "alert": true}, "fav": {"email": true, "label": "Desea recibir una notificacion cuando agregan un aviso propio a favoritos", "alert": true}, "msg": {"email": true, "label": "Desea recibir una notificacion cuando recibe un mensaje", "alert": true}, "prox": {"email": true, "label": "Desea recibir una notificacion cuando estas cerca de uno de tus avisos favoritos", "alert": true}, "cal": {"email": true, "label": "Desea recibir una notificacion cuando tiene tiene la posibilidad de calificar a otro usuario", "alert": true}}	1
2	{"msg": {"email": true, "alert": true, "label": "Desea recibir una notificacion cuando recibe un mensaje"}, "fav": {"email": true, "alert": true, "label": "Desea recibir una notificacion cuando agregan un aviso propio a favoritos"}, "prox": {"email": true, "alert": true, "label": "Desea recibir una notificacion cuando estas cerca de uno de tus avisos favoritos"}, "cmmt": {"email": true, "alert": true, "label": "Desea recibir una notificacion cuando commentan un aviso propio"}, "cal": {"email": true, "alert": true, "label": "Desea recibir una notificacion cuando tiene tiene la posibilidad de calificar a otro usuario"}}	2
3	{"msg": {"email": true, "alert": true, "label": "Desea recibir una notificacion cuando recibe un mensaje"}, "fav": {"email": true, "alert": true, "label": "Desea recibir una notificacion cuando agregan un aviso propio a favoritos"}, "prox": {"email": true, "alert": true, "label": "Desea recibir una notificacion cuando estas cerca de uno de tus avisos favoritos"}, "cmmt": {"email": true, "alert": true, "label": "Desea recibir una notificacion cuando commentan un aviso propio"}, "cal": {"email": true, "alert": true, "label": "Desea recibir una notificacion cuando tiene tiene la posibilidad de calificar a otro usuario"}}	3
4	{"msg": {"email": true, "alert": true, "label": "Desea recibir una notificacion cuando recibe un mensaje"}, "fav": {"email": true, "alert": true, "label": "Desea recibir una notificacion cuando agregan un aviso propio a favoritos"}, "prox": {"email": true, "alert": true, "label": "Desea recibir una notificacion cuando estas cerca de uno de tus avisos favoritos"}, "cmmt": {"email": true, "alert": true, "label": "Desea recibir una notificacion cuando commentan un aviso propio"}, "cal": {"email": true, "alert": true, "label": "Desea recibir una notificacion cuando tiene tiene la posibilidad de calificar a otro usuario"}}	4
\.


--
-- Name: notification_confignotification_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('notification_confignotification_id_seq', 4, true);


--
-- Data for Name: notification_notification; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY notification_notification (id, type, message, created, extras, read, receiver_id) FROM stdin;
\.


--
-- Name: notification_notification_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('notification_notification_id_seq', 1, false);


--
-- Data for Name: push_notifications_apnsdevice; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY push_notifications_apnsdevice (id, name, active, date_created, device_id, registration_id, user_id) FROM stdin;
\.


--
-- Name: push_notifications_apnsdevice_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('push_notifications_apnsdevice_id_seq', 1, false);


--
-- Data for Name: push_notifications_gcmdevice; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY push_notifications_gcmdevice (id, name, active, date_created, device_id, registration_id, user_id) FROM stdin;
\.


--
-- Name: push_notifications_gcmdevice_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('push_notifications_gcmdevice_id_seq', 1, false);


--
-- Data for Name: rating_overallrating; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY rating_overallrating (id, rate, user_id) FROM stdin;
\.


--
-- Name: rating_overallrating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('rating_overallrating_id_seq', 1, false);


--
-- Data for Name: rating_rating; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY rating_rating (id, transaction_id, state, rate, created, transaction_type_id, voted_id, voter_id) FROM stdin;
\.


--
-- Name: rating_rating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('rating_rating_id_seq', 1, false);


--
-- Data for Name: report_error_errorreport; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY report_error_errorreport (id, description, date, screenshot) FROM stdin;
1	Una vez que le doy buscar direccion, si muevo el mara y vuelvo a apretar la lupita, no me reposiciona	2015-12-01 12:33:02.325626-05	report/temp_ftiJ8Rx.png
\.


--
-- Name: report_error_errorreport_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('report_error_errorreport_id_seq', 1, true);


--
-- Data for Name: socialaccount_socialaccount; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY socialaccount_socialaccount (id, provider, uid, last_login, date_joined, extra_data, user_id) FROM stdin;
1	facebook	10205471498440309	2015-12-01 12:29:16.225527-05	2015-12-01 12:29:16.225609-05	{"name": "Marcos Barroso", "first_name": "Marcos", "verified": true, "link": "https://www.facebook.com/app_scoped_user_id/10205471498440309/", "timezone": -3, "last_name": "Barroso", "locale": "es_LA", "email": "mj1182@hotmail.com", "gender": "male", "id": "10205471498440309", "updated_time": "2015-04-09T20:43:45+0000"}	4
\.


--
-- Name: socialaccount_socialaccount_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('socialaccount_socialaccount_id_seq', 1, true);


--
-- Data for Name: socialaccount_socialapp; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY socialaccount_socialapp (id, provider, name, client_id, secret, key) FROM stdin;
1	facebook	Facebook App	381267902068971	b3e7774c39b93ccd782ca4934f74fba0	
2	google	Google App	426322048378-h8tjb2ckn6lsadkai106g0gpqvnpvgd3.apps.googleusercontent.com	OfaLpvS2kzwQhzAA3x06INBs	
\.


--
-- Name: socialaccount_socialapp_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('socialaccount_socialapp_id_seq', 2, true);


--
-- Data for Name: socialaccount_socialapp_sites; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY socialaccount_socialapp_sites (id, socialapp_id, site_id) FROM stdin;
1	1	1
2	2	1
\.


--
-- Name: socialaccount_socialapp_sites_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('socialaccount_socialapp_sites_id_seq', 2, true);


--
-- Data for Name: socialaccount_socialtoken; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY socialaccount_socialtoken (id, token, token_secret, expires_at, account_id, app_id) FROM stdin;
1	CAAFawtndZBOsBAAFpyknZCZA1thHPvdrT4NBPqKKrA0RT2Aztk3uZBShO7PltpfBZC0yotU3xA5DymVJmeV4LYZAycTwbstBiKW9GhgIfWyrE3WIhDWKrCTJSOVbr9f8uu3xIuyCa7K9xs5AY6N2lVKcHBnGYc6AZAOhExE5rv2cpVQBqhZBKglZBUfsIq94RNvMZD		\N	1	1
\.


--
-- Name: socialaccount_socialtoken_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('socialaccount_socialtoken_id_seq', 1, true);


--
-- Data for Name: taggit_tag; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY taggit_tag (id, name, slug) FROM stdin;
1	Equipo	equipo
2	de	de
3	GNC	gnc
4	5ta	5ta
5	Generación	generacion
6	Pinza	pinza
7	Amperometrica	amperometrica
8	Micrometro	micrometro
9	0-25	0-25
10	mm	mm
11	X	x
12	0.01	001
13	Juego	juego
14	6	6
15	llaves	llaves
16		
17	MARCA	marca
18	BANGO	bango
\.


--
-- Name: taggit_tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('taggit_tag_id_seq', 18, true);


--
-- Data for Name: taggit_taggeditem; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY taggit_taggeditem (id, object_id, content_type_id, tag_id) FROM stdin;
1	1	25	1
2	1	25	2
3	1	25	3
4	1	25	4
5	1	25	5
6	2	25	6
7	2	25	7
8	3	25	8
9	3	25	9
10	3	25	10
11	3	25	11
12	3	25	12
13	4	25	13
14	4	25	2
15	4	25	14
16	4	25	15
17	4	25	16
18	4	25	17
19	4	25	18
\.


--
-- Name: taggit_taggeditem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('taggit_taggeditem_id_seq', 19, true);


--
-- Data for Name: thumbnail_kvstore; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY thumbnail_kvstore (key, value) FROM stdin;
sorl-thumbnail||image||3a46ecb2b961f3c7051affca232e4398	{"name": "profile/default.jpg", "size": [700, 700], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||71c3671c0668568267ba8f9c0d470f33	{"name": "cache/de/78/de78265a475140a452ca90c7ec23369a.png", "size": [400, 400], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||thumbnails||3a46ecb2b961f3c7051affca232e4398	["71c3671c0668568267ba8f9c0d470f33"]
sorl-thumbnail||image||df996797c41d65f76d2d633adf486df1	{"name": "ad/gnc1.jpg", "size": [715, 600], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||6e35b099b1d58eb64f69e12aa278311b	{"name": "cache/1d/a2/1da26f03e87ff855e0116e67226a9c74.png", "size": [110, 110], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||thumbnails||df996797c41d65f76d2d633adf486df1	["6e35b099b1d58eb64f69e12aa278311b"]
sorl-thumbnail||image||c559bc4fad8290047d5661dc58414ce6	{"name": "cache/95/d6/95d68d617102615dbc5bd86f7effb15a.png", "size": [800, 800], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||3420d57b6217bb049f92d737da75cbe4	{"name": "cache/d2/e4/d2e4a6708abe9ce2159c30907ab1765c.png", "size": [800, 800], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||1ccb59f5147f6e152d482ee544e85311	{"name": "cache/31/8e/318ea8385e74e3961b0d1c13798d1543.png", "size": [110, 110], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||926717880272e18637bb941e2dccf888	{"name": "ad/GEDC1938.JPG", "size": [3240, 4320], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||7a66d6c6d990ffb5ac0b98fbc449cda0	{"name": "cache/60/dc/60dcc07b61eecb4bb17efcc449258874.png", "size": [110, 110], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||thumbnails||926717880272e18637bb941e2dccf888	["7a66d6c6d990ffb5ac0b98fbc449cda0"]
sorl-thumbnail||image||9969e33dab4205d341417678ff596343	{"name": "cache/0c/1e/0c1e3312993fa8dca8d9f052611022d5.png", "size": [800, 800], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||d093790c57ac63a7596b9371d09e72a9	{"name": "ad/GEDC1939.JPG", "size": [3240, 4320], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||24c32993f2f5b82f668fc99d4442983f	{"name": "cache/f6/83/f68301933a3083829ba68963e034d2d9.png", "size": [110, 110], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||thumbnails||d093790c57ac63a7596b9371d09e72a9	["24c32993f2f5b82f668fc99d4442983f"]
sorl-thumbnail||image||f58518db3b50d854c041fc395a6346b2	{"name": "cache/b4/4b/b44bf13a5e9f4e17402ad5a6a90342bd.png", "size": [800, 800], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||45299b62a7bbbbc7dc9dafe0bdbe9aed	{"name": "ad/GEDC1940.JPG", "size": [3240, 4320], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||5d0da150c2964bc22a198b6d7afc9c1d	{"name": "cache/f6/23/f6231cb82e9a071623f40de357df9361.png", "size": [110, 110], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||thumbnails||45299b62a7bbbbc7dc9dafe0bdbe9aed	["5d0da150c2964bc22a198b6d7afc9c1d"]
sorl-thumbnail||image||90f17250941027d30332b46222280bf4	{"name": "cache/d1/f9/d1f9938be02e31405ee706ca94d785df.png", "size": [800, 800], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||8f9ae08c526d1cdb7193700e8268bf1a	{"name": "ad/GEDC1935.JPG", "size": [4320, 3240], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||311345f845c7b2fabb035989989ea144	{"name": "cache/8a/43/8a43f15535e99b98891c71ce6c831c9e.png", "size": [110, 110], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||thumbnails||8f9ae08c526d1cdb7193700e8268bf1a	["311345f845c7b2fabb035989989ea144"]
sorl-thumbnail||image||60e683c7fcc88752fc517f01ed918c63	{"name": "cache/c9/04/c904ee71dd23fbf9ab15416d08858680.png", "size": [800, 800], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||723fbe3784bbcbc6d9e5ae3bcf39634a	{"name": "ad/GEDC1936.JPG", "size": [4320, 3240], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||7bfa68cd21e29c26c4a45bc52b1d2571	{"name": "cache/e3/df/e3df7095ab2660ca98c960fa4cef3666.png", "size": [110, 110], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||thumbnails||723fbe3784bbcbc6d9e5ae3bcf39634a	["7bfa68cd21e29c26c4a45bc52b1d2571"]
sorl-thumbnail||image||ae986529af8c09a06fc4fef94bc27ab8	{"name": "cache/72/5c/725c9dfa3e343c07564b29a6bab78f97.png", "size": [800, 800], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||0767de10efc18e14fc3855a4187404e9	{"name": "ad/GEDC1937.JPG", "size": [4320, 3240], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||345a8884630ed4a885d3e72c1e85f21e	{"name": "cache/50/69/5069cd41a9e68d9f6672a46bc5cfa00b.png", "size": [110, 110], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||thumbnails||0767de10efc18e14fc3855a4187404e9	["345a8884630ed4a885d3e72c1e85f21e"]
sorl-thumbnail||image||22a3e697e833e368847e422dde35e989	{"name": "cache/3d/11/3d111997f82e9ddbda120275333bc86d.png", "size": [800, 800], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||c8a3811a31274eb697f1b0b24c843009	{"name": "ad/GEDC1941.JPG", "size": [4320, 3240], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||6e4266003a19ee8f80122d178862848d	{"name": "cache/01/82/01822270ff9e652cc332f09a533ed467.png", "size": [110, 110], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||thumbnails||c8a3811a31274eb697f1b0b24c843009	["6e4266003a19ee8f80122d178862848d"]
sorl-thumbnail||image||fd05d9ac13def99efa439348456c4991	{"name": "cache/c0/54/c054ca15895330d800d337d76bd63fc8.png", "size": [800, 800], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||d33e6483c644b2ea359111a4d6e0ed70	{"name": "ad/GEDC1942.JPG", "size": [4320, 3240], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||75a2fa569676a65c3508aac0f5502cfa	{"name": "cache/48/1f/481ffad0cf656163b660af67274fd860.png", "size": [110, 110], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||thumbnails||d33e6483c644b2ea359111a4d6e0ed70	["75a2fa569676a65c3508aac0f5502cfa"]
sorl-thumbnail||image||f43bf9985ffd9c83a60de9ec541c9f01	{"name": "cache/53/48/534878cade2ed3980da6f5850a88d4ca.png", "size": [800, 800], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||3aea68b90fcf0c78a2c29332581f1e60	{"name": "ad/GEDC1943.JPG", "size": [4320, 3240], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||59e09d720c347dfcd8468133620a423e	{"name": "cache/6e/9c/6e9caa01204a4148eb76e75f99400733.png", "size": [110, 110], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||thumbnails||3aea68b90fcf0c78a2c29332581f1e60	["59e09d720c347dfcd8468133620a423e"]
sorl-thumbnail||image||e1b84927165665fc0c84d600794cd4dc	{"name": "cache/fd/ee/fdeef062ee2088f3ecfca7a5b881554e.png", "size": [800, 800], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||f3933777ca59cc20ebe2743fd7073a12	{"name": "ad/GEDC1945.JPG", "size": [4320, 3240], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||379a0e1699cf358c43c594b448e2cb73	{"name": "cache/0c/22/0c226ee9f3abeaa97c89db722ae2d7d0.png", "size": [110, 110], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||thumbnails||f3933777ca59cc20ebe2743fd7073a12	["379a0e1699cf358c43c594b448e2cb73"]
sorl-thumbnail||image||09f9a54b1caf10312d6ec0a4549356bb	{"name": "cache/08/0d/080d78ac88991a2c1c13e8ec7345978f.png", "size": [800, 800], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||ce9c4e88f0afe8e6e1e7bd7931f9f04d	{"name": "cache/02/48/0248b03abf6717ec4db89eeb514ebefd.png", "size": [800, 800], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||8d4dde9cfd7ffc4ec6a31bae555a70ab	{"name": "cache/01/03/0103f38cef5eae8b78a8b9e20a72f660.png", "size": [110, 110], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||8fcf5321f21cc799f475e456f25a0713	{"name": "cache/9d/4e/9d4e229dd7bdb63c4dbd570aa678d89c.png", "size": [800, 800], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||9b5c8aae736b257dbbe7c24a2ef745b4	{"name": "cache/ee/4e/ee4ed08b1106f8ebcd62d164396b14bf.png", "size": [110, 110], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||d1c02ac416f2502b6a1a3a50ba2b8907	{"name": "cache/8d/c2/8dc2a509a8f45c979bf503e9289f8944.png", "size": [800, 800], "storage": "django.core.files.storage.FileSystemStorage"}
sorl-thumbnail||image||6f83233df30c457113f0629e4f2a009a	{"name": "cache/2c/2c/2c2c1f6b66ccb214eb355d7b4ed3572c.png", "size": [110, 110], "storage": "django.core.files.storage.FileSystemStorage"}
\.


--
-- Data for Name: userProfile_phone; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY "userProfile_phone" (id, number, type, "userProfile_id") FROM stdin;
\.


--
-- Name: userProfile_phone_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('"userProfile_phone_id_seq"', 1, false);


--
-- Data for Name: userProfile_store; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY "userProfile_store" (slug, id, logo, name, slogan, style, status, profile_id) FROM stdin;
	1				{"column": 4, "background_color": "#f9f9f9", "font_color": "#00000"}	0	1
	2				{"font_color": "#00000", "column": 4, "background_color": "#f9f9f9"}	0	2
	3				{"font_color": "#00000", "column": 4, "background_color": "#f9f9f9"}	0	3
	4				{"font_color": "#00000", "column": 4, "background_color": "#f9f9f9"}	0	4
\.


--
-- Name: userProfile_store_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('"userProfile_store_id_seq"', 4, true);


--
-- Data for Name: userProfile_userlocation; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY "userProfile_userlocation" (id, title, lat, lng, radius, is_address, address, "userProfile_id") FROM stdin;
1	aaaaaaaaa	-31.4085549999999998	-64.2188274999999749	5000	t	{"locality": "C\\u00f3rdoba", "administrative_area_level_2": "Capital", "country": "Argentina", "nro": 22, "address": "2222222222", "administrative_area_level_1": "C\\u00f3rdoba"}	1
2	Negocio	-13.3027200000000008	-87.1441070000000053	5000	t	{"administrative_area_level_2": "", "nro": 935, "administrative_area_level_1": "", "address": "27 de Abril", "locality": "", "country": ""}	2
3	Mi dpto	-31.4183008000000008	-64.1891714999999863	5000	t	{"administrative_area_level_2": "Capital", "nro": 274, "administrative_area_level_1": "C\\u00f3rdoba", "address": "Duarte Quiros", "locality": "C\\u00f3rdoba", "country": "Argentina"}	3
\.


--
-- Name: userProfile_userlocation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('"userProfile_userlocation_id_seq"', 3, true);


--
-- Data for Name: userProfile_userprofile; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY "userProfile_userprofile" (id, image, birth_date, privacy_settings, user_id) FROM stdin;
1	profile/default.jpg	\N	{"show_address": true}	1
2	profile/default.jpg	\N	{"show_address": true}	2
3	profile/default.jpg	\N	{"show_address": true}	3
4	profile/default.jpg	\N	{"show_address": true}	4
\.


--
-- Name: userProfile_userprofile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('"userProfile_userprofile_id_seq"', 4, true);


--
-- Data for Name: util_counterwhered; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY util_counterwhered (id, whered, counter) FROM stdin;
\.


--
-- Name: util_counterwhered_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('util_counterwhered_id_seq', 1, false);


--
-- Data for Name: util_interested; Type: TABLE DATA; Schema: public; Owner: compraloahi
--

COPY util_interested (id, email, seller, buyer, android, ios) FROM stdin;
\.


--
-- Name: util_interested_id_seq; Type: SEQUENCE SET; Schema: public; Owner: compraloahi
--

SELECT pg_catalog.setval('util_interested_id_seq', 1, false);


--
-- Name: account_emailaddress_email_key; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY account_emailaddress
    ADD CONSTRAINT account_emailaddress_email_key UNIQUE (email);


--
-- Name: account_emailaddress_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY account_emailaddress
    ADD CONSTRAINT account_emailaddress_pkey PRIMARY KEY (id);


--
-- Name: account_emailconfirmation_key_key; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY account_emailconfirmation
    ADD CONSTRAINT account_emailconfirmation_key_key UNIQUE (key);


--
-- Name: account_emailconfirmation_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY account_emailconfirmation
    ADD CONSTRAINT account_emailconfirmation_pkey PRIMARY KEY (id);


--
-- Name: adLocation_adlocation_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY "adLocation_adlocation"
    ADD CONSTRAINT "adLocation_adlocation_pkey" PRIMARY KEY (id);


--
-- Name: ad_ad_categories_ad_id_category_id_key; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY ad_ad_categories
    ADD CONSTRAINT ad_ad_categories_ad_id_category_id_key UNIQUE (ad_id, category_id);


--
-- Name: ad_ad_categories_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY ad_ad_categories
    ADD CONSTRAINT ad_ad_categories_pkey PRIMARY KEY (id);


--
-- Name: ad_ad_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY ad_ad
    ADD CONSTRAINT ad_ad_pkey PRIMARY KEY (id);


--
-- Name: ad_adimage_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY ad_adimage
    ADD CONSTRAINT ad_adimage_pkey PRIMARY KEY (id);


--
-- Name: ad_category_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY ad_category
    ADD CONSTRAINT ad_category_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: authtoken_token_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY authtoken_token
    ADD CONSTRAINT authtoken_token_pkey PRIMARY KEY (key);


--
-- Name: authtoken_token_user_id_key; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id);


--
-- Name: corsheaders_corsmodel_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY corsheaders_corsmodel
    ADD CONSTRAINT corsheaders_corsmodel_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_comment_flags_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY django_comment_flags
    ADD CONSTRAINT django_comment_flags_pkey PRIMARY KEY (id);


--
-- Name: django_comment_flags_user_id_5111a19327627901_uniq; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY django_comment_flags
    ADD CONSTRAINT django_comment_flags_user_id_5111a19327627901_uniq UNIQUE (user_id, comment_id, flag);


--
-- Name: django_comments_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY django_comments
    ADD CONSTRAINT django_comments_pkey PRIMARY KEY (id);


--
-- Name: django_comments_xtd_xtdcomment_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY django_comments_xtd_xtdcomment
    ADD CONSTRAINT django_comments_xtd_xtdcomment_pkey PRIMARY KEY (comment_ptr_id);


--
-- Name: django_content_type_app_label_5b4222e888ab2920_uniq; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_5b4222e888ab2920_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- Name: djmail_message_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY djmail_message
    ADD CONSTRAINT djmail_message_pkey PRIMARY KEY (uuid);


--
-- Name: faq_question_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY faq_question
    ADD CONSTRAINT faq_question_pkey PRIMARY KEY (id);


--
-- Name: faq_question_slug_key; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY faq_question
    ADD CONSTRAINT faq_question_slug_key UNIQUE (slug);


--
-- Name: faq_questionscore_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY faq_questionscore
    ADD CONSTRAINT faq_questionscore_pkey PRIMARY KEY (id);


--
-- Name: faq_topic_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY faq_topic
    ADD CONSTRAINT faq_topic_pkey PRIMARY KEY (id);


--
-- Name: favorite_favorite_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY favorite_favorite
    ADD CONSTRAINT favorite_favorite_pkey PRIMARY KEY (id);


--
-- Name: favorite_favorite_user_id_3fc2251fcf1d6fd8_uniq; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY favorite_favorite
    ADD CONSTRAINT favorite_favorite_user_id_3fc2251fcf1d6fd8_uniq UNIQUE (user_id, target_content_type_id, target_object_id);


--
-- Name: msg_msg_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY msg_msg
    ADD CONSTRAINT msg_msg_pkey PRIMARY KEY (id);


--
-- Name: notification_confignotification_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY notification_confignotification
    ADD CONSTRAINT notification_confignotification_pkey PRIMARY KEY (id);


--
-- Name: notification_confignotification_user_id_key; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY notification_confignotification
    ADD CONSTRAINT notification_confignotification_user_id_key UNIQUE (user_id);


--
-- Name: notification_notification_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY notification_notification
    ADD CONSTRAINT notification_notification_pkey PRIMARY KEY (id);


--
-- Name: push_notifications_apnsdevice_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY push_notifications_apnsdevice
    ADD CONSTRAINT push_notifications_apnsdevice_pkey PRIMARY KEY (id);


--
-- Name: push_notifications_apnsdevice_registration_id_key; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY push_notifications_apnsdevice
    ADD CONSTRAINT push_notifications_apnsdevice_registration_id_key UNIQUE (registration_id);


--
-- Name: push_notifications_gcmdevice_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY push_notifications_gcmdevice
    ADD CONSTRAINT push_notifications_gcmdevice_pkey PRIMARY KEY (id);


--
-- Name: rating_overallrating_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY rating_overallrating
    ADD CONSTRAINT rating_overallrating_pkey PRIMARY KEY (id);


--
-- Name: rating_overallrating_user_id_key; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY rating_overallrating
    ADD CONSTRAINT rating_overallrating_user_id_key UNIQUE (user_id);


--
-- Name: rating_rating_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY rating_rating
    ADD CONSTRAINT rating_rating_pkey PRIMARY KEY (id);


--
-- Name: report_error_errorreport_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY report_error_errorreport
    ADD CONSTRAINT report_error_errorreport_pkey PRIMARY KEY (id);


--
-- Name: socialaccount_socialaccount_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY socialaccount_socialaccount
    ADD CONSTRAINT socialaccount_socialaccount_pkey PRIMARY KEY (id);


--
-- Name: socialaccount_socialaccount_provider_7f8864a934115b0c_uniq; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY socialaccount_socialaccount
    ADD CONSTRAINT socialaccount_socialaccount_provider_7f8864a934115b0c_uniq UNIQUE (provider, uid);


--
-- Name: socialaccount_socialapp_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY socialaccount_socialapp
    ADD CONSTRAINT socialaccount_socialapp_pkey PRIMARY KEY (id);


--
-- Name: socialaccount_socialapp_sites_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY socialaccount_socialapp_sites
    ADD CONSTRAINT socialaccount_socialapp_sites_pkey PRIMARY KEY (id);


--
-- Name: socialaccount_socialapp_sites_socialapp_id_site_id_key; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY socialaccount_socialapp_sites
    ADD CONSTRAINT socialaccount_socialapp_sites_socialapp_id_site_id_key UNIQUE (socialapp_id, site_id);


--
-- Name: socialaccount_socialtoken_app_id_4a6d793fcc5f6694_uniq; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY socialaccount_socialtoken
    ADD CONSTRAINT socialaccount_socialtoken_app_id_4a6d793fcc5f6694_uniq UNIQUE (app_id, account_id);


--
-- Name: socialaccount_socialtoken_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY socialaccount_socialtoken
    ADD CONSTRAINT socialaccount_socialtoken_pkey PRIMARY KEY (id);


--
-- Name: taggit_tag_name_key; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY taggit_tag
    ADD CONSTRAINT taggit_tag_name_key UNIQUE (name);


--
-- Name: taggit_tag_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY taggit_tag
    ADD CONSTRAINT taggit_tag_pkey PRIMARY KEY (id);


--
-- Name: taggit_tag_slug_key; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY taggit_tag
    ADD CONSTRAINT taggit_tag_slug_key UNIQUE (slug);


--
-- Name: taggit_taggeditem_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY taggit_taggeditem
    ADD CONSTRAINT taggit_taggeditem_pkey PRIMARY KEY (id);


--
-- Name: thumbnail_kvstore_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY thumbnail_kvstore
    ADD CONSTRAINT thumbnail_kvstore_pkey PRIMARY KEY (key);


--
-- Name: userProfile_phone_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY "userProfile_phone"
    ADD CONSTRAINT "userProfile_phone_pkey" PRIMARY KEY (id);


--
-- Name: userProfile_store_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY "userProfile_store"
    ADD CONSTRAINT "userProfile_store_pkey" PRIMARY KEY (id);


--
-- Name: userProfile_store_profile_id_key; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY "userProfile_store"
    ADD CONSTRAINT "userProfile_store_profile_id_key" UNIQUE (profile_id);


--
-- Name: userProfile_userlocation_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY "userProfile_userlocation"
    ADD CONSTRAINT "userProfile_userlocation_pkey" PRIMARY KEY (id);


--
-- Name: userProfile_userprofile_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY "userProfile_userprofile"
    ADD CONSTRAINT "userProfile_userprofile_pkey" PRIMARY KEY (id);


--
-- Name: userProfile_userprofile_user_id_key; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY "userProfile_userprofile"
    ADD CONSTRAINT "userProfile_userprofile_user_id_key" UNIQUE (user_id);


--
-- Name: util_counterwhered_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY util_counterwhered
    ADD CONSTRAINT util_counterwhered_pkey PRIMARY KEY (id);


--
-- Name: util_counterwhered_whered_key; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY util_counterwhered
    ADD CONSTRAINT util_counterwhered_whered_key UNIQUE (whered);


--
-- Name: util_interested_email_key; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY util_interested
    ADD CONSTRAINT util_interested_email_key UNIQUE (email);


--
-- Name: util_interested_pkey; Type: CONSTRAINT; Schema: public; Owner: compraloahi; Tablespace: 
--

ALTER TABLE ONLY util_interested
    ADD CONSTRAINT util_interested_pkey PRIMARY KEY (id);


--
-- Name: account_emailaddress_e8701ad4; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX account_emailaddress_e8701ad4 ON account_emailaddress USING btree (user_id);


--
-- Name: account_emailaddress_email_7aeafff06d46e9fa_like; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX account_emailaddress_email_7aeafff06d46e9fa_like ON account_emailaddress USING btree (email varchar_pattern_ops);


--
-- Name: account_emailconfirmation_6f1edeac; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX account_emailconfirmation_6f1edeac ON account_emailconfirmation USING btree (email_address_id);


--
-- Name: account_emailconfirmation_key_2b7edf72e860b742_like; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX account_emailconfirmation_key_2b7edf72e860b742_like ON account_emailconfirmation USING btree (key varchar_pattern_ops);


--
-- Name: adLocation_adlocation_411f412e; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX "adLocation_adlocation_411f412e" ON "adLocation_adlocation" USING btree (ad_id);


--
-- Name: ad_ad_2dbcba41; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX ad_ad_2dbcba41 ON ad_ad USING btree (slug);


--
-- Name: ad_ad_4f331e2f; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX ad_ad_4f331e2f ON ad_ad USING btree (author_id);


--
-- Name: ad_ad_categories_411f412e; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX ad_ad_categories_411f412e ON ad_ad_categories USING btree (ad_id);


--
-- Name: ad_ad_categories_b583a629; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX ad_ad_categories_b583a629 ON ad_ad_categories USING btree (category_id);


--
-- Name: ad_ad_slug_1f50665db594dbdf_like; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX ad_ad_slug_1f50665db594dbdf_like ON ad_ad USING btree (slug varchar_pattern_ops);


--
-- Name: ad_adimage_0c8dd491; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX ad_adimage_0c8dd491 ON ad_adimage USING btree (ad_id_id);


--
-- Name: ad_category_2dbcba41; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX ad_category_2dbcba41 ON ad_category USING btree (slug);


--
-- Name: ad_category_slug_4c3b9a0ae6f6aa32_like; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX ad_category_slug_4c3b9a0ae6f6aa32_like ON ad_category USING btree (slug varchar_pattern_ops);


--
-- Name: auth_group_name_4a5c5a1f233424ac_like; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX auth_group_name_4a5c5a1f233424ac_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_0e939a4f; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX auth_group_permissions_0e939a4f ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_8373b171; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX auth_group_permissions_8373b171 ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_417f1b1c; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX auth_permission_417f1b1c ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_0e939a4f; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX auth_user_groups_0e939a4f ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_e8701ad4; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX auth_user_groups_e8701ad4 ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_8373b171; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_8373b171 ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_e8701ad4; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_e8701ad4 ON auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_462a93f0916a2e91_like; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX auth_user_username_462a93f0916a2e91_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- Name: authtoken_token_key_47e9c21d94115dad_like; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX authtoken_token_key_47e9c21d94115dad_like ON authtoken_token USING btree (key varchar_pattern_ops);


--
-- Name: django_admin_log_417f1b1c; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX django_admin_log_417f1b1c ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_e8701ad4; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX django_admin_log_e8701ad4 ON django_admin_log USING btree (user_id);


--
-- Name: django_comment_flags_327a6c43; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX django_comment_flags_327a6c43 ON django_comment_flags USING btree (flag);


--
-- Name: django_comment_flags_69b97d17; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX django_comment_flags_69b97d17 ON django_comment_flags USING btree (comment_id);


--
-- Name: django_comment_flags_e8701ad4; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX django_comment_flags_e8701ad4 ON django_comment_flags USING btree (user_id);


--
-- Name: django_comment_flags_flag_6fad4d083b46c28a_like; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX django_comment_flags_flag_6fad4d083b46c28a_like ON django_comment_flags USING btree (flag varchar_pattern_ops);


--
-- Name: django_comments_417f1b1c; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX django_comments_417f1b1c ON django_comments USING btree (content_type_id);


--
-- Name: django_comments_9365d6e7; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX django_comments_9365d6e7 ON django_comments USING btree (site_id);


--
-- Name: django_comments_e8701ad4; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX django_comments_e8701ad4 ON django_comments USING btree (user_id);


--
-- Name: django_comments_xtd_xtdcomment_70a17ffa; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX django_comments_xtd_xtdcomment_70a17ffa ON django_comments_xtd_xtdcomment USING btree ("order");


--
-- Name: django_comments_xtd_xtdcomment_e3464c97; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX django_comments_xtd_xtdcomment_e3464c97 ON django_comments_xtd_xtdcomment USING btree (thread_id);


--
-- Name: django_session_de54fa62; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX django_session_de54fa62 ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_3460c011aa9416a5_like; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX django_session_session_key_3460c011aa9416a5_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: djmail_message_uuid_54aba741cfec0247_like; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX djmail_message_uuid_54aba741cfec0247_like ON djmail_message USING btree (uuid varchar_pattern_ops);


--
-- Name: faq_question_19b4d727; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX faq_question_19b4d727 ON faq_question USING btree (topic_id);


--
-- Name: faq_question_9ccf0ba6; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX faq_question_9ccf0ba6 ON faq_question USING btree (updated_by_id);


--
-- Name: faq_question_e93cb7eb; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX faq_question_e93cb7eb ON faq_question USING btree (created_by_id);


--
-- Name: faq_question_slug_6bb99b045d328296_like; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX faq_question_slug_6bb99b045d328296_like ON faq_question USING btree (slug varchar_pattern_ops);


--
-- Name: faq_questionscore_7aa0f6ee; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX faq_questionscore_7aa0f6ee ON faq_questionscore USING btree (question_id);


--
-- Name: faq_questionscore_e8701ad4; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX faq_questionscore_e8701ad4 ON faq_questionscore USING btree (user_id);


--
-- Name: faq_topic_2dbcba41; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX faq_topic_2dbcba41 ON faq_topic USING btree (slug);


--
-- Name: faq_topic_9365d6e7; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX faq_topic_9365d6e7 ON faq_topic USING btree (site_id);


--
-- Name: faq_topic_9ccf0ba6; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX faq_topic_9ccf0ba6 ON faq_topic USING btree (updated_by_id);


--
-- Name: faq_topic_e93cb7eb; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX faq_topic_e93cb7eb ON faq_topic USING btree (created_by_id);


--
-- Name: faq_topic_slug_765a058d1e8e416d_like; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX faq_topic_slug_765a058d1e8e416d_like ON faq_topic USING btree (slug varchar_pattern_ops);


--
-- Name: favorite_favorite_d7e6d55b; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX favorite_favorite_d7e6d55b ON favorite_favorite USING btree ("timestamp");


--
-- Name: favorite_favorite_e4f9dcc7; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX favorite_favorite_e4f9dcc7 ON favorite_favorite USING btree (target_content_type_id);


--
-- Name: favorite_favorite_e8701ad4; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX favorite_favorite_e8701ad4 ON favorite_favorite USING btree (user_id);


--
-- Name: msg_msg_417f1b1c; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX msg_msg_417f1b1c ON msg_msg USING btree (content_type_id);


--
-- Name: msg_msg_6be37982; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX msg_msg_6be37982 ON msg_msg USING btree (parent_id);


--
-- Name: msg_msg_8b938c66; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX msg_msg_8b938c66 ON msg_msg USING btree (recipient_id);


--
-- Name: msg_msg_924b1846; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX msg_msg_924b1846 ON msg_msg USING btree (sender_id);


--
-- Name: msg_msg_e3464c97; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX msg_msg_e3464c97 ON msg_msg USING btree (thread_id);


--
-- Name: notification_notification_d41c2251; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX notification_notification_d41c2251 ON notification_notification USING btree (receiver_id);


--
-- Name: push_notifications_apnsde_registration_id_1b85a53696b21f24_like; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX push_notifications_apnsde_registration_id_1b85a53696b21f24_like ON push_notifications_apnsdevice USING btree (registration_id varchar_pattern_ops);


--
-- Name: push_notifications_apnsdevice_9379346c; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX push_notifications_apnsdevice_9379346c ON push_notifications_apnsdevice USING btree (device_id);


--
-- Name: push_notifications_apnsdevice_e8701ad4; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX push_notifications_apnsdevice_e8701ad4 ON push_notifications_apnsdevice USING btree (user_id);


--
-- Name: push_notifications_gcmdevice_9379346c; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX push_notifications_gcmdevice_9379346c ON push_notifications_gcmdevice USING btree (device_id);


--
-- Name: push_notifications_gcmdevice_e8701ad4; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX push_notifications_gcmdevice_e8701ad4 ON push_notifications_gcmdevice USING btree (user_id);


--
-- Name: rating_rating_49fb0f8b; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX rating_rating_49fb0f8b ON rating_rating USING btree (voter_id);


--
-- Name: rating_rating_69b792c7; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX rating_rating_69b792c7 ON rating_rating USING btree (voted_id);


--
-- Name: rating_rating_92c431dc; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX rating_rating_92c431dc ON rating_rating USING btree (transaction_type_id);


--
-- Name: socialaccount_socialaccount_e8701ad4; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX socialaccount_socialaccount_e8701ad4 ON socialaccount_socialaccount USING btree (user_id);


--
-- Name: socialaccount_socialapp_sites_9365d6e7; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX socialaccount_socialapp_sites_9365d6e7 ON socialaccount_socialapp_sites USING btree (site_id);


--
-- Name: socialaccount_socialapp_sites_fe95b0a0; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX socialaccount_socialapp_sites_fe95b0a0 ON socialaccount_socialapp_sites USING btree (socialapp_id);


--
-- Name: socialaccount_socialtoken_8a089c2a; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX socialaccount_socialtoken_8a089c2a ON socialaccount_socialtoken USING btree (account_id);


--
-- Name: socialaccount_socialtoken_f382adfe; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX socialaccount_socialtoken_f382adfe ON socialaccount_socialtoken USING btree (app_id);


--
-- Name: taggit_tag_name_cabb71f3de40695_like; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX taggit_tag_name_cabb71f3de40695_like ON taggit_tag USING btree (name varchar_pattern_ops);


--
-- Name: taggit_tag_slug_5c1f7310c84c01cc_like; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX taggit_tag_slug_5c1f7310c84c01cc_like ON taggit_tag USING btree (slug varchar_pattern_ops);


--
-- Name: taggit_taggeditem_417f1b1c; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX taggit_taggeditem_417f1b1c ON taggit_taggeditem USING btree (content_type_id);


--
-- Name: taggit_taggeditem_76f094bc; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX taggit_taggeditem_76f094bc ON taggit_taggeditem USING btree (tag_id);


--
-- Name: taggit_taggeditem_af31437c; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX taggit_taggeditem_af31437c ON taggit_taggeditem USING btree (object_id);


--
-- Name: thumbnail_kvstore_key_6ca8b872df0a465b_like; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX thumbnail_kvstore_key_6ca8b872df0a465b_like ON thumbnail_kvstore USING btree (key varchar_pattern_ops);


--
-- Name: userProfile_phone_9ebcc067; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX "userProfile_phone_9ebcc067" ON "userProfile_phone" USING btree ("userProfile_id");


--
-- Name: userProfile_store_2dbcba41; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX "userProfile_store_2dbcba41" ON "userProfile_store" USING btree (slug);


--
-- Name: userProfile_store_slug_d32377de7c6094b_like; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX "userProfile_store_slug_d32377de7c6094b_like" ON "userProfile_store" USING btree (slug varchar_pattern_ops);


--
-- Name: userProfile_userlocation_9ebcc067; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX "userProfile_userlocation_9ebcc067" ON "userProfile_userlocation" USING btree ("userProfile_id");


--
-- Name: util_counterwhered_whered_ac66cbe5ad263df_like; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX util_counterwhered_whered_ac66cbe5ad263df_like ON util_counterwhered USING btree (whered varchar_pattern_ops);


--
-- Name: util_interested_email_503088fbc5aadebe_like; Type: INDEX; Schema: public; Owner: compraloahi; Tablespace: 
--

CREATE INDEX util_interested_email_503088fbc5aadebe_like ON util_interested USING btree (email varchar_pattern_ops);


--
-- Name: acc_email_address_id_72acb02afdf1890_fk_account_emailaddress_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY account_emailconfirmation
    ADD CONSTRAINT acc_email_address_id_72acb02afdf1890_fk_account_emailaddress_id FOREIGN KEY (email_address_id) REFERENCES account_emailaddress(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_emailaddress_user_id_3e706a8a4df88dfe_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY account_emailaddress
    ADD CONSTRAINT account_emailaddress_user_id_3e706a8a4df88dfe_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: adLocation_adlocation_ad_id_6f44fad8a4836125_fk_ad_ad_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY "adLocation_adlocation"
    ADD CONSTRAINT "adLocation_adlocation_ad_id_6f44fad8a4836125_fk_ad_ad_id" FOREIGN KEY (ad_id) REFERENCES ad_ad(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ad_ad_author_id_709cc9611b8b84c0_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY ad_ad
    ADD CONSTRAINT ad_ad_author_id_709cc9611b8b84c0_fk_auth_user_id FOREIGN KEY (author_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ad_ad_categories_ad_id_6c46c42c0e73bc93_fk_ad_ad_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY ad_ad_categories
    ADD CONSTRAINT ad_ad_categories_ad_id_6c46c42c0e73bc93_fk_ad_ad_id FOREIGN KEY (ad_id) REFERENCES ad_ad(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ad_ad_categories_category_id_72f8b8fb1159071a_fk_ad_category_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY ad_ad_categories
    ADD CONSTRAINT ad_ad_categories_category_id_72f8b8fb1159071a_fk_ad_category_id FOREIGN KEY (category_id) REFERENCES ad_category(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ad_adimage_ad_id_id_6f4098dbc951fac2_fk_ad_ad_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY ad_adimage
    ADD CONSTRAINT ad_adimage_ad_id_id_6f4098dbc951fac2_fk_ad_ad_id FOREIGN KEY (ad_id_id) REFERENCES ad_ad(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_content_type_id_706b8ece59ffc83e_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_content_type_id_706b8ece59ffc83e_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissio_group_id_3563518380174fe8_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_group_id_3563518380174fe8_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permission_id_68aaf7e9df974a52_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permission_id_68aaf7e9df974a52_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_7d44442f0b49010f_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_7d44442f0b49010f_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_user_id_3c520a5116775617_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_3c520a5116775617_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_u_permission_id_65614c889a0fdf0_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_u_permission_id_65614c889a0fdf0_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permiss_user_id_262fd35b1a93b792_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permiss_user_id_262fd35b1a93b792_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authtoken_token_user_id_1f568c7fd741dbc8_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_1f568c7fd741dbc8_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: djan_content_type_id_10cdfd7351cca30e_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY django_comments
    ADD CONSTRAINT djan_content_type_id_10cdfd7351cca30e_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: djan_content_type_id_255e80e38e3c24d9_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT djan_content_type_id_255e80e38e3c24d9_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_69530b183ad17040_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_69530b183ad17040_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_co_comment_ptr_id_31bb939d3226eac9_fk_django_comments_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY django_comments_xtd_xtdcomment
    ADD CONSTRAINT django_co_comment_ptr_id_31bb939d3226eac9_fk_django_comments_id FOREIGN KEY (comment_ptr_id) REFERENCES django_comments(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_commen_comment_id_3bfd40f9565879d7_fk_django_comments_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY django_comment_flags
    ADD CONSTRAINT django_commen_comment_id_3bfd40f9565879d7_fk_django_comments_id FOREIGN KEY (comment_id) REFERENCES django_comments(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_comment_flags_user_id_5cb40ad765ef1e5b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY django_comment_flags
    ADD CONSTRAINT django_comment_flags_user_id_5cb40ad765ef1e5b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_comments_site_id_b7c3be4a2388b7c_fk_django_site_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY django_comments
    ADD CONSTRAINT django_comments_site_id_b7c3be4a2388b7c_fk_django_site_id FOREIGN KEY (site_id) REFERENCES django_site(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_comments_user_id_2dfb00ad8fc1898d_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY django_comments
    ADD CONSTRAINT django_comments_user_id_2dfb00ad8fc1898d_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ed86613fd3c29b8b76d1f0a74f2b7866; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY favorite_favorite
    ADD CONSTRAINT ed86613fd3c29b8b76d1f0a74f2b7866 FOREIGN KEY (target_content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: faq_question_created_by_id_311a164557af74b8_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY faq_question
    ADD CONSTRAINT faq_question_created_by_id_311a164557af74b8_fk_auth_user_id FOREIGN KEY (created_by_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: faq_question_topic_id_480cf652e7d34594_fk_faq_topic_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY faq_question
    ADD CONSTRAINT faq_question_topic_id_480cf652e7d34594_fk_faq_topic_id FOREIGN KEY (topic_id) REFERENCES faq_topic(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: faq_question_updated_by_id_4cdc0572e2f95624_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY faq_question
    ADD CONSTRAINT faq_question_updated_by_id_4cdc0572e2f95624_fk_auth_user_id FOREIGN KEY (updated_by_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: faq_questionsco_question_id_7ced95f317c9ce86_fk_faq_question_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY faq_questionscore
    ADD CONSTRAINT faq_questionsco_question_id_7ced95f317c9ce86_fk_faq_question_id FOREIGN KEY (question_id) REFERENCES faq_question(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: faq_questionscore_user_id_6418d85baaaf1030_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY faq_questionscore
    ADD CONSTRAINT faq_questionscore_user_id_6418d85baaaf1030_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: faq_topic_created_by_id_364e40543608391b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY faq_topic
    ADD CONSTRAINT faq_topic_created_by_id_364e40543608391b_fk_auth_user_id FOREIGN KEY (created_by_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: faq_topic_site_id_71e70c0b232659a4_fk_django_site_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY faq_topic
    ADD CONSTRAINT faq_topic_site_id_71e70c0b232659a4_fk_django_site_id FOREIGN KEY (site_id) REFERENCES django_site(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: faq_topic_updated_by_id_74184e7ef200b43f_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY faq_topic
    ADD CONSTRAINT faq_topic_updated_by_id_74184e7ef200b43f_fk_auth_user_id FOREIGN KEY (updated_by_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: favorite_favorite_user_id_4cab8753437366e1_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY favorite_favorite
    ADD CONSTRAINT favorite_favorite_user_id_4cab8753437366e1_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: msg__content_type_id_69729395353819ae_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY msg_msg
    ADD CONSTRAINT msg__content_type_id_69729395353819ae_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: msg_msg_parent_id_656edf2c6ae7987b_fk_msg_msg_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY msg_msg
    ADD CONSTRAINT msg_msg_parent_id_656edf2c6ae7987b_fk_msg_msg_id FOREIGN KEY (parent_id) REFERENCES msg_msg(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: msg_msg_recipient_id_245f49bad7f73c31_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY msg_msg
    ADD CONSTRAINT msg_msg_recipient_id_245f49bad7f73c31_fk_auth_user_id FOREIGN KEY (recipient_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: msg_msg_sender_id_33710909ea7306d5_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY msg_msg
    ADD CONSTRAINT msg_msg_sender_id_33710909ea7306d5_fk_auth_user_id FOREIGN KEY (sender_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: msg_msg_thread_id_7c2339d62908e4b0_fk_msg_msg_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY msg_msg
    ADD CONSTRAINT msg_msg_thread_id_7c2339d62908e4b0_fk_msg_msg_id FOREIGN KEY (thread_id) REFERENCES msg_msg(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: notification_confignot_user_id_407606e30a7518b7_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY notification_confignotification
    ADD CONSTRAINT notification_confignot_user_id_407606e30a7518b7_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: notification_notif_receiver_id_75467efa530d174b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY notification_notification
    ADD CONSTRAINT notification_notif_receiver_id_75467efa530d174b_fk_auth_user_id FOREIGN KEY (receiver_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: push_notifications_apn_user_id_3e6a91f9fa01811d_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY push_notifications_apnsdevice
    ADD CONSTRAINT push_notifications_apn_user_id_3e6a91f9fa01811d_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: push_notifications_gcm_user_id_437746fe8f040a07_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY push_notifications_gcmdevice
    ADD CONSTRAINT push_notifications_gcm_user_id_437746fe8f040a07_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: rating_overallrating_user_id_120bee0950585f0_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY rating_overallrating
    ADD CONSTRAINT rating_overallrating_user_id_120bee0950585f0_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: rating_rating_voted_id_6fbf7e07bcbd6397_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY rating_rating
    ADD CONSTRAINT rating_rating_voted_id_6fbf7e07bcbd6397_fk_auth_user_id FOREIGN KEY (voted_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: rating_rating_voter_id_e2906e2527f0bff_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY rating_rating
    ADD CONSTRAINT rating_rating_voter_id_e2906e2527f0bff_fk_auth_user_id FOREIGN KEY (voter_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: so_account_id_d899db70eb9cb73_fk_socialaccount_socialaccount_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY socialaccount_socialtoken
    ADD CONSTRAINT so_account_id_d899db70eb9cb73_fk_socialaccount_socialaccount_id FOREIGN KEY (account_id) REFERENCES socialaccount_socialaccount(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: soc_socialapp_id_1f3a97cc561ee3b2_fk_socialaccount_socialapp_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY socialaccount_socialapp_sites
    ADD CONSTRAINT soc_socialapp_id_1f3a97cc561ee3b2_fk_socialaccount_socialapp_id FOREIGN KEY (socialapp_id) REFERENCES socialaccount_socialapp(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: socialacc_app_id_396d870d2b54c29e_fk_socialaccount_socialapp_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY socialaccount_socialtoken
    ADD CONSTRAINT socialacc_app_id_396d870d2b54c29e_fk_socialaccount_socialapp_id FOREIGN KEY (app_id) REFERENCES socialaccount_socialapp(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: socialaccount_social_site_id_73974afb01939452_fk_django_site_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY socialaccount_socialapp_sites
    ADD CONSTRAINT socialaccount_social_site_id_73974afb01939452_fk_django_site_id FOREIGN KEY (site_id) REFERENCES django_site(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: socialaccount_socialac_user_id_6447aa748cc3abe0_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY socialaccount_socialaccount
    ADD CONSTRAINT socialaccount_socialac_user_id_6447aa748cc3abe0_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tagg_content_type_id_2c32bfd45b4a21c1_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY taggit_taggeditem
    ADD CONSTRAINT tagg_content_type_id_2c32bfd45b4a21c1_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: taggit_taggeditem_tag_id_65c5a97e3f3a7854_fk_taggit_tag_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY taggit_taggeditem
    ADD CONSTRAINT taggit_taggeditem_tag_id_65c5a97e3f3a7854_fk_taggit_tag_id FOREIGN KEY (tag_id) REFERENCES taggit_tag(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: transaction_type_id_702cf82ff4d30715_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY rating_rating
    ADD CONSTRAINT transaction_type_id_702cf82ff4d30715_fk_django_content_type_id FOREIGN KEY (transaction_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: u_userProfile_id_312638ff20312fba_fk_userProfile_userprofile_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY "userProfile_userlocation"
    ADD CONSTRAINT "u_userProfile_id_312638ff20312fba_fk_userProfile_userprofile_id" FOREIGN KEY ("userProfile_id") REFERENCES "userProfile_userprofile"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: u_userProfile_id_3e5bd7c7703cf06d_fk_userProfile_userprofile_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY "userProfile_phone"
    ADD CONSTRAINT "u_userProfile_id_3e5bd7c7703cf06d_fk_userProfile_userprofile_id" FOREIGN KEY ("userProfile_id") REFERENCES "userProfile_userprofile"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: userP_profile_id_227e61a11e828f87_fk_userProfile_userprofile_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY "userProfile_store"
    ADD CONSTRAINT "userP_profile_id_227e61a11e828f87_fk_userProfile_userprofile_id" FOREIGN KEY (profile_id) REFERENCES "userProfile_userprofile"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: userProfile_userprofil_user_id_46ce6ef2b7db9391_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: compraloahi
--

ALTER TABLE ONLY "userProfile_userprofile"
    ADD CONSTRAINT "userProfile_userprofil_user_id_46ce6ef2b7db9391_fk_auth_user_id" FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

